#!/bin/bash

# Inicia el servidor ZooKeeper (necesario para Kafka)
/opt/kafka_2.12-3.6.0/bin/zookeeper-server-start.sh /opt/kafka_2.12-3.6.0/config/zookeeper.properties &

# Espera unos segundos para asegurarse de que ZooKeeper esté en funcionamiento
sleep 5

# Inicia el servidor Kafka
/opt/kafka_2.12-3.6.0/bin/kafka-server-start.sh /opt/kafka_2.12-3.6.0/config/server.properties

