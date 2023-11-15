import datetime
import json
import logging
from kafka import KafkaConsumer
import psycopg2

year_part = 1
month_part = 2
day_part = 3
hour_part = 4
minute_part = 5

# Configura el nivel de registro
logging.basicConfig(level=logging.INFO)


def build_kpi_value(timestamp, parts):
    date = str(datetime.datetime.fromtimestamp(timestamp)).split(" ")
    dateparts = date[0].split("-") + date[1].split(":")
    return "".join(dateparts[0:parts])


def store_kpi(kpi_key, kpi_value, vcount):
    sql = """
    INSERT INTO test.kpis(kpi_key, kpi_value, vcount) VALUES ( %s, %s, %s )
    ON CONFLICT ( kpi_key, kpi_value )
    DO UPDATE SET vcount = kpis.vcount + EXCLUDED.vcount;
    """
    cur.execute(sql, (kpi_key, kpi_value, vcount))
    conn.commit()


print('Connecting to the database...')

# Conexión a la base de datos
conn = psycopg2.connect(
    database="postgresdb",
    host="127.0.0.1",
    user="postgres",
    password="postgres",
    port="5432"
)
cur = conn.cursor()
print('Connected to the database!')

# Conexión al servidor Kafka
consumer = KafkaConsumer(
    group_id='my-group',
    bootstrap_servers=['127.0.0.1:29092'],
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print('Connected to Kafka...')
consumer.subscribe(topics=['test'])
print('Subscribed to Kafka topic...')

for msg in consumer:
    print('Initializing processing...')
    logging.info("{0}".format(msg))

    # Registro de mensajes de información adicionales
    logging.info("Received message: {0}".format(msg.value))
    logging.info("Timestamp: {0}".format(msg.value["@timestamp"]))

    store_kpi(
        "REQUEST_X_MINUTE",
        build_kpi_value(msg.value["@timestamp"], minute_part),
        1
    )
    print('Processing request per minute initialized...')

    store_kpi(
        "REQUEST_X_HOUR",
        build_kpi_value(msg.value["@timestamp"], hour_part),
        1
    )
    print('Processing request per hour initialized...')

    store_kpi(
        "REQUEST_X_DAY",
        build_kpi_value(msg.value["@timestamp"], day_part),
        1
    )
    print('Processing request per day initialized...')
