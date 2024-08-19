## Kafka and Zookeeper Installation

### Requirement :

- fedora 40
- java 8
- Scala 2.13 (bundled)

### Step :
1. Download binary from apache :
    ```
    wget https://archive.apache.org/dist/kafka/2.8.2/kafka_2.13-2.8.2.tgz
    ```

2. Extract the package :
    ```
    tar -xvf kafka_2.13-2.8.2.tgz
    cd kafka_2.13-2.8.2
    ```

3. add kafka to systemd :
    ```
    [Unit]
    Description=Apache Kafka Server
    Documentation=http://kafka.apache.org/documentation.html
    Requires=zookeeper.service

    [Service]
    Type=simple
    ExecStart=<home-kafka>/bin/kafka-server-start.sh <home-kafka>/config/server.properties
    ExecStop=<home-kafka>/bin/kafka-server-stop.sh
    ```
4. add zookeeper to systemd :
    ```
    [Unit]
    Description=Apache Zookeeper server
    Documentation=http://zookeeper.apache.org
    Requires=network.target remote-fs.target
    After=network.target remote-fs.target

    [Service]
    Type=simple
    ExecStart=<kafka-home>/bin/zookeeper-server-start.sh <kafka-home>/config/zookeeper.properties
    ExecStop=<kafka-home>/bin/zookeeper-server-stop.sh
    Restart=on-abnormal

    [Install]
    WantedBy=multi-user.target

    ```
3. Reload daemon and start kafka & zk :
    ```
    systemctl daemon reload
    systemctl start kafka
    ```
    
3. Once the kafka started,  we can test to enter kafka console with this following command :
    ```
    ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic btc_prices --from-beginning
    ```