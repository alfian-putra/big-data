
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
#from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
#from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.operators.mysql_operator import MySqlOperator 
#from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from time import strftime

#defining target pageview tarbal name
target_day = int(strftime("%d"))
target_hour = int(strftime("%H")) - 9
if target_hour<=0 or target_hour==24 :
    if target_hour==0:
        target_hour = -1
    target_day = target_day -1
    target_hour = 24 + target_hour

target_day = str(target_day)
target_hour = str(target_hour) if len(str(target_hour))>=2 else "0"+str(target_hour)

pageview_tarbal = "pageviews-{{ execution_date.year }}{{ '{:02}'.format(execution_date.month) }}"+target_day+"-"+target_hour+"0000.gz "
#Defining DAG
dag = DAG(
  dag_id="wikipediaPageViews",
  start_date=airflow.utils.dates.days_ago(0),
  schedule_interval="@once",
  catchup=False,
  template_searchpath="/tmp"
)

#Task 1: Obtain Data from source
get_data = BashOperator(
  task_id="get_data",
  bash_command=(
    "wget -O /tmp/"
    #"pageviews-{{ execution_date.year }}"
    #"{{ '{:02}'.format(execution_date.month) }}"
    #"{{ '{:02}'.format(execution_date.day) }}-"
    #+target_hour+".gz "
    "pageview.gz "
    "https://dumps.wikimedia.org/other/pageviews/"
    "{{ execution_date.year }}/"
    "{{ execution_date.year }}-"
    "{{ '{:02}'.format(execution_date.month) }}/"
    +pageview_tarbal

  ),
  dag=dag,
)

#Task 2: Unzip the extracted file
extract_gz = BashOperator(
    task_id="extract_gz",
    bash_command="gunzip --force /tmp/pageview.gz",
    #"pageviews-{{ execution_date.year }}"
    #"{{ '{:02}'.format(execution_date.month) }}"
    #"{{ '{:02}'.format(execution_date.day) }}-"
    #+target_hour+".gz",

    dag=dag,
)

#Python callable function used in Python operator
def _fetch_pageviews(pagenames,**context):
    result = dict.fromkeys(pagenames, 0)
    with open(f"/tmp/pageview", "r") as f:
        for line in f:
            domain_code, page_title, view_counts, _ = line.split(" ")
            if domain_code == "en" and page_title in pagenames:
                result[page_title] = view_counts

    with open(f"/tmp/sqlserver_query.sql", "w") as f:
       f.write(f"Delete from pageview_counts where datetime='{context['execution_date']}';")
       for pagename, pageviewcount in result.items():
           f.write(
               "INSERT INTO pageview_counts VALUES ("
               f"'{pagename}', {pageviewcount}, '{context['execution_date']}'"
               ");\n"
           )

#Task 3: Perform transformation and generate sql script
fetch_pageviews = PythonOperator(
    task_id="fetch_pageviews",
    python_callable=_fetch_pageviews,
    op_kwargs={
        "pagenames": {
            "Google",
            "Amazon",
            "Apple",
            "Microsoft",
            "Facebook",
        }
    },
    dag=dag,
)

#Task 4: Inserts data into SQL server
write_to_sqlserever = MySqlOperator(
   task_id="write_to_sqlserever",
   mysql_conn_id="conn_example_mysql",
   sql="sqlserver_query.sql",
   database="wikipageview",
   dag=dag,
)

#Defining task dependencies
get_data>>extract_gz>>fetch_pageviews>>write_to_sqlserever
