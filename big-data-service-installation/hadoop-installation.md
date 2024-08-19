## Hadoop installation

### Requirement :

- fedora 40
- ssh
- java 8

### Note :
hadoop on single node cluster

### Step :

1. install java openjdk
    ```
    yum install -y java-1.8.0-openjdk \
                java-1.8.0-openjdk-headless \
                java-1.8.0-openjdk-devel 
    ```
2. Create ssh passwordless 
    ```
    ssh-keygen -t rsa -m PEM -b 3072 # empty the passphrase step (i use the default configuration or empty every step)
    ssh-copy-id root@localhost
    ```
    __-t :__ algorithm that will be applied

    __-m :__ key format in this chase the key will be .pem
    
    __-b :__ key length in bit

3. Download the binary file from apache
    ```
    wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
    ```
4. extract the downloaded file end cd to extracted dir
    ```
    tar -xvf hadoop-3.3.4.tar.gz
    cd hadoop-3.3.4/
    ```
5. Add configuration to setup default filesystem when we using hdfs command
    ```
    vi etc/hadoop/core-site.xml
    ```
    add this following configuration :
    ```
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://localhost:9000</value>
        </property>
    </configuration>
    ```
6. setup siongle node configuration
    ```
    vi etc/hadoop/hdfs-site.xml
    ```
    add this following configuration :
    ```
    <configuration>
        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
    </configuration>

    ```
8. Configure the user add JAVA_HOME (__NOTE :___ I recommend using this following JOAVA_HOME , i encounter error (JAVA_HOME not be found or set) although define the JAVA_HOME that point to correct dir but it didnt work, and it solved by using this configuration)
    ```
    vi etc/hadoop/hadoop-env.sh
    ```

    ```
    export HDFS_NAMENODE_USER="root"
    export HDFS_DATANODE_USER="root"
    export HDFS_SECONDARYNAMENODE_USER="root"
    export YARN_RESOURCEMANAGER_USER="root"
    export YARN_NODEMANAGER_USER="root"
    export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
    ```

7. initialize namenode
    ```
    bin/hdfs namenode -format
    ```
8. Start whole service
    ```
    sbin/start-all.sh
    ```

