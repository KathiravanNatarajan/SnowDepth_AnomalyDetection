In this project, We focus on detecting the anomalies in snow depth. 

  Install Docker for Windows: https://docs.docker.com/desktop/install/windows-install/
  Install miniKube for Windows: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download

Assuming the docker and miniKube are installed on the Windows machine. 

1. docker-compose.yaml - Use the docker-compose file to install the Apache Kafka with the ZooKeeper dependency. 
  The command to run this file is docker-compose up, which spins up the containers. This file creates the network for the Kafka containers.
2. Dockerfile - use the docker file to build producer and consumer container images. 
     docker build -t . will build the image for the producer and consumer. 
4. producer.py - Runs the producer container, which utilizes the snow depth data to generate and stream the data to the consumer containers, which are listening to the same topic
5. consumer.py - Listens to the Kafka topic and makes the function call to detect the anomaly in the snow depth using the K-Means clustering algorithm 
6. unsupervised.py—Kmeans clustering code to run the anomaly detection algorithm. This code is experimental, and the model trained from it is further updated in consumer.py to detect anomalies in the snow depth. 
If you want to run the containers separately by deploying it using the miniKube, you can run the producer and consumer using the following command. 
docker run --network kafka-qt_kafka-network -it producer-code /bin/bash # kafka-qt_kafka-network is created to make sure all the containers are running in the same network 

#############################################################################################

#### Some useful Docker commands: 

docker stop $(docker ps -q) # To stop all running containers 
docker system prune -a --volumes # System wide cleanup 
docker exec -it 0d96feee8680 /bin/bash # To run the container interactively 
docker build -t <image-name>:<tag> . # Docker build on a docker file

#### Some Kubernetes commands to deploy and verify: 

kubectl apply -f deployment.yaml # deploy the containers 
kubectl get deployments
kubectl get pods
kubectl get services
kubectl scale - to scale 

##############################################################################################
