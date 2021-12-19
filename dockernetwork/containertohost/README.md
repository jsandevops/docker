# Docker Network: Request from container to World Wide Web (Externally hosted API) 

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockernetwork/containertohost `  

## Build a docker image:  
> ` docker build -t dockernetworktohost:1 . `  

## Install Postgres DB on local
> `docker run -d --name host-postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=dockerpass -e POSTGRES_USER=dockeruser -e POSTGRES_DB=dockerdb postgres:alpine3.15 `  

Postgres DB will be used from Docker container however, we will be connecting to it as if it is an independent service

## Check images:
> ` docker image ls `  

## Run container from image:
> ` docker run -d --rm -p 9091:9091 --name=dockernetworktohost dockernetworktohost:1 `    

## Send request to API:
> ` curl localhost:9091 `   
> ` curl localhost:9091/details `  

## **Conclusion:**
- Container cannot connect to local running services with *localhost*  
- Container can connect to local running service with special domain *host.docker.internal*  
