# Docker Network: Request from container to another container using IP address

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockernetwork/containertocontainer/option1withip `  

## Build a docker image:  
> ` docker build -t dockernetworktocontainerwithip:1 . `  

## Check images:
> ` docker image ls ` 

## Install Postgres DB on local
> ` docker run -d --rm -p 5432:5432 --name container-postgres-db -e POSTGRES_PASSWORD=dockerpass -e POSTGRES_USER=dockeruser -e POSTGRES_DB=dockerdb postgres:alpine3.15 ` 

In this case, Postgres DB will be used as another container 

## Find IP Address for Postgress which is running as another containwe
> ` docker inspect container-postgres-db | findstr IPAddress `  

## Run container from image and replace IP address of Postgres DB container in POSTGRES_IP variable:
> ` docker run -d --rm -p 9091:9091 -e POSTGRES_IP=172.17.0.2 --name=dockernetworktocontainerwithip dockernetworktocontainerwithip:1 `    

## Send request to API:
> ` curl localhost:9091 `   
> ` curl localhost:9091/details `  

## **Conclusion:**
- Container can communicate with each other using IP address. However this is not recommended way as IP address can change if container is restarted  
