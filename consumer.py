from confluent_kafka import Consumer, KafkaException
import sys

def consume_messages():
    kafka_broker = 'kafka:9092'
    kafka_topic = 'test'
    group_id = 'test-consumer-group'

    # Consumer configuration
    conf = {
        'bootstrap.servers': kafka_broker,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)

    # Subscribe to topic
    consumer.subscribe([kafka_topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_messages()
