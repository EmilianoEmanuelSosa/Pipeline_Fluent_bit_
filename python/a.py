import logging
from kafka import KafkaConsumer

# Configuración de registro (logs)
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de registro: DEBUG para mensajes detallados
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Crear un objeto de registro para este script
logger = logging.getLogger(__name__)

# Configuración de Kafka Consumer
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode("utf-8")
)

try:
    for msg in consumer:
        # Imprimir el mensaje recibido en el tópico 'test'
        logger.info("Mensaje recibido: %s", msg.value)

except KeyboardInterrupt:
    # Manejar la interrupción del usuario (Ctrl+C) para detener el consumidor
    pass

finally:
    # Cerrar el consumidor de Kafka
    consumer.close()

