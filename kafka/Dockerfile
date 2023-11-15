# Utiliza una imagen base de Ubuntu
FROM ubuntu:latest

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    openjdk-8-jre-headless \
    wget \
    netcat # Agregamos netcat como herramienta adicional

# Descarga e instala Kafka
WORKDIR /opt
RUN wget -q https://downloads.apache.org/kafka/3.6.0/kafka_2.12-3.6.0.tgz && \
    tar -xzf kafka_2.12-3.6.0.tgz && \
    rm kafka_2.12-3.6.0.tgz

# Expone el puerto de Kafka (generalmente el 9092)
EXPOSE 9092

# Copia el archivo de inicio personalizado
COPY entrypoint.sh /opt

# Configura el archivo de inicio personalizado como ejecutable
RUN chmod +x /opt/entrypoint.sh

# Comando para iniciar Kafka
CMD ["/opt/entrypoint.sh"]

