# flask-asset-demo
A demo on how to store and retrieve binary files using
PostgreSQL, SQLAlchemy, and Flask.  This demo shows store assets both in
a database(currently supported) and on the filesystem/S3 (can be added later) using SQLAlchemy.  


## Installation
1. create k8s cluster using minikube/EKS/AKS <br />
2. Install kubectl and clone the github repository <br />
3. kubectl create -f k8s-deploy/db-pod.yaml <br />
4. kubectl create -f k8s-deploy/db-service.yaml <br />
5. kubectl create -f web-Deployment.yaml <br />
6. kubectl create -f crytogen-service.yaml <br />

## Steps:
1.Created Kubernetes Cluster on Azure using AKS and Terraform. <br />
2.deployed vault Secret Engine and Consul for Secret Storage, I used cubbyhole as secret Engine. <br />
3.Hosted Redis(concurrent request processing using REDIS_QUEUE ,rq ) and Mysql on Azure for secret storage and secret processing. <br />
4.developed frontend application using FLASK and SQLAlchemy for Interacting for Secret Storage <br />

## K8s cluster on Azure
![Alt text](static/images/k8s_cluster.png?raw=true "k8s_cluster")

## Adding Asset
![Alt text](static/images/store_asset.png?raw=true "store_asset")

## Getting the task status
![Alt text](static/images/task_status.png?raw=true "task_status")
![Alt text](static/images/task_completed.png?raw=true "task_completed")

## added into database
![Alt text](static/images/added_to_db.png?raw=true "added_to_db")

## added into secret Engine
![Alt text](static/images/assets_secretengine.png?raw=true "get assets from secretEngine")

## List of assets
![Alt text](static/images/asset_list.png?raw=true "get assets from db")

## Clean UP
kubectl delete -f k8s-deploy/
