## Spark Binnary Installation

### Requirement :

- fedora 40
- java 8

### NOTE :
SPark need hadoop and scala but in this installation we will use Spark that was bundled with with hadoop and scala within, therefore i dont add it as a requirement.

### Step :

1. Download binary from apache :
    ```
    https://archive.apache.org/dist/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3-scala2.13.tgz
    ```

2. Extract the package :
    ```
    tar -xvf spark-3.4.0-bin-hadoop3-scala2.13.tgz
    ```

3. edit .bash_profile to export the bin command to make the linux can run the script from any dir :
    ```
    export PATH=$PATH:<path-extracted-spark>/spark-3.4.0-bin-hadoop3-scala2.13/bin
    ```
4. RUn this to apply the export :
    ```
    export ~/.bash_profile
    ```

5. Now check the spark using following command :
    ```
    spark-shell
    ```

    It's should be return this following output :

    ```
    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    24/07/04 22:49:09 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    Spark context Web UI available at http://playground.id:4040
    Spark context available as 'sc' (master = local[*], app id = local-1720108163557).
    Spark session available as 'spark'.
    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /___/ .__/\_,_/_/ /_/\_\   version 3.4.0
          /_/

    Using Scala version 2.12.17 (OpenJDK 64-Bit Server VM, Java 1.8.0_412)
    Type in expressions to have them evaluated.
    Type :help for more information.

    scala>
    ```