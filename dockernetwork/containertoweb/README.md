# Docker Network: Request from container to World Wide Web (Externally hosted API) 

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockernetwork/containertoweb `  

## Build a docker image:  
> ` docker build -t dockernetworktoweb:1 . `  
  
## Check images:
> ` docker image ls `  

## Run container from image:
> ` docker run -d --rm -p 9091:9091 --name=dockernetworktoweb dockernetworktoweb:1 `    

## Send request to API:
> ` curl localhost:9091 `   
> ` curl localhost:9091/details `  

## **Conclusion:**
- By default containers can send request to World Wide Web  
