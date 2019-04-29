# flask-asset-demo
A demo on how to store and retrieve binary files using
PostgreSQL, SQLAlchemy, and Flask.  This demo shows store assets both in
a database(currently supported) and on the filesystem/S3 (can be added later) using SQLAlchemy.  


## Installation

pip install -r requirements.txt <br />
python manage.py db upgrade <br />
python worker.py <br />
python manage.py runserver <br />


And finally, browse to [http://localhost:5000/](http://localhost:5000).

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
