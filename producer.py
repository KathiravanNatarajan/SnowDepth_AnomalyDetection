from confluent_kafka import Producer
import time
import pandas as pd
import json
import random
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result. """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')
        
# def generate_message():
#
#     # timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#     # random_number = random.randint(1, 1000)
#     # message = f"Hello from Kathir, again! Timestamp: {timestamp}, Random Number: {random_number}"
#     # return message.encode('utf-8')
#     return

def produce_messages():
    # Kafka broker configuration
    kafka_broker = 'kafka:9092'
    # Kafka topic to produce to
    kafka_topic = 'test'

    # Create Producer instance
    producer = Producer({
        'bootstrap.servers': kafka_broker
    })

    df = pd.read_csv("./snowdepth-sample.csv")
    # Optional: Define delivery callback to track delivery results
    #producer.produce(kafka_topic, key=None, value="Hell0 from Kathir, again!", callback=delivery_report)
    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
        # Convert the row to a string or a specific format as needed
        row_dict = row.to_dict()
        # Convert the dictionary to a JSON string
        message = json.dumps(row_dict)
        producer.produce(kafka_topic, value=message, callback=delivery_report)
        time.sleep(10)
        # producer.produce(kafka_topic, value=generate_message(), callback=delivery_report)
    # Flush the producer to ensure all messages are delivered before closing
    producer.flush()

if __name__ == '__main__':
    produce_messages()
