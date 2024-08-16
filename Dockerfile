# Dockerfile for producer container
FROM python:3.8-slim

WORKDIR /app

# Copy producer script and requirements
COPY consumer.py /app

# Install dependencies
RUN pip install confluent_kafka

CMD ["python", "consumer.py"]

#
# #Dockerfile for producer container
# FROM python:3.8-slim
#
# WORKDIR /app
#
# # Copy the datafile
# COPY snowdepth-sample.csv /app
#
# # Copy producer script and requirements
# COPY producer.py /app
#
# # Install dependencies
# RUN pip install confluent_kafka
# RUN pip install pandas
#
# CMD ["python", "producer.py"]

