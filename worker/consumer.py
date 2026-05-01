from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "product_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Kafka consumer running...")

for msg in consumer:
    print("EVENT:", msg.value)
