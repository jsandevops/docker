# Docker Network: Request from container to another container using network

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockernetwork/containertocontainer/option2withnetwork `  

## Build a docker image:  
> ` docker build -t dockernetworktocontainerwithnetwork:1 . `  

## Check images:
> ` docker image ls ` 

## Create a network:
> ` docker network create mynetwork `  
> ` docker network ls `  

Networks are not created automatically unlike volumes

## Install Postgres DB on local
> ` docker run -d --rm -p 5432:5432 --network mynetwork --name container-postgres-db -e POSTGRES_PASSWORD=dockerpass -e POSTGRES_USER=dockeruser -e POSTGRES_DB=dockerdb postgres:alpine3.15 ` 

In this case, Postgres DB will be used as another container 

## Run container from image and replace POSTGRES_SERVICE_NAME variable with Postgress container name:
> ` docker run -d --rm -p 9091:9091 --network mynetwork -e POSTGRES_SERVICE_NAME=container-postgres-db --name=dockernetworktocontainerwithnetwork dockernetworktocontainerwithnetwork:1 `    

Note: --network tag is added here in both the above run commands

## Send request to API:
> ` curl localhost:9091 `   
> ` curl localhost:9091/details `  

## **Conclusion:**
- Container can communicate with each other using container name as host incase both are part of same network  
