## Airflow installation on virtual environment 

### Requirement :

- fedora 40
- python3 (3.12)
- python3-devel
- python3-pip
- gcc

### Step :

1. Preparing the directory :

    ```
    mkdir ~/service &&  cd ~/service 
    ```

2. Make a venv

    ```
    python3 -m venv airflow
    ```

3. Activate venv

    ```
    source .airflow/bin/source
    ```

4. Install apache airflow

    ```
    pip install apache-airflow==2.9.1
    ```

5. Creating controller file

    ```
    cd ..
    touch start_airflow.sh
    chmod +x start_airflow.sh\
    ```
6. make a miscelanous dir to support *`start_airflow.sh`* functionality 

    ```
    mkdir log_services pid_services
    ```

7. Add this following line to the script *`start_airflow.sh`*

    ```
    #!/usr/bin/bash

    export PYTHONPATH=<venv-dir>/bin/*:<venv-dir>/lib/python3.12/site-packages/*:$PYTHONPATH
    export AIRFLOW_HOME=<venv-dir>
    export PATH=$PATH:$AIRFLOW_HOME/bin
    export OUT_FILE=./log_services/airflow.out
    export LOG_FILE=./log_services/airflow.log
    export PID_FILE=./pid_services/airflow.pid
    # optional -> export VENV_AIRFLOW=<venv-dir>/bin/activate

    source services_bigdata/airflow/bin/activate ; export AIRFLOW_CONFIG=<venv-dir>/airflow.cfg && $AIRFLOW_HOME/bin/airflow standalone > $OUT_FILE  2> $LOG_FILE & echo $! > $PID_FILE

    # optional (to show venv) -> echo "Using venv :"
    # optional (to show venv) -> echo $VENV_AIRFLOW

    cat $PID_FILE
    ```
9. Access airflow ui in http://localhost:8080 login access (__user and password/passphrase__) can be found in log file.
8. Now we can start the airflow using *`start_airflow.sh`* script, this will start airflow in standalone mode, the log will be redirected to *`log_services`* as *`airflow.out`* and *`airflow.log`*.

    ```
    ./strart_airflow.sh
    ```

9. To stop airflow we can kill pid, that will be saved on *`pid_services`* with name *`airtflow.pid`* to make it easy, we can create *`stop_airflow.sh`*, that contain following command :

    ```
    #!/usr/bin/bash

    export PID_FILE=./pid_services/airflow.pid

    export PID_AIRFLOW=$(cat $PID_FILE)

    kill $PID_AIRFLOW
    
    ```
10. Now we can stop airflow with the script

    ```
    ./stop_airflow.sh
    ```

### Adds-on Operator :

1. celery

    Requirement :
    - gcc

    Installation :

    ```
    pip install 'apache-airflow[celery]'
    ```

2. mysqlOperator

    Requirement :
    - mariadb-devel

    Installation :

    ```
    pip install apache-airflow-providers-mysql
    ```
