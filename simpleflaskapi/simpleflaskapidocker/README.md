# Simple Flask API Dockerised

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/simpleflaskapi/simpleflaskapidocker `  

## Build a docker image:  
> ` docker build -t simpleflaskapidocker:2 . `  
  
## Check images:
> ` docker image ls `  

## Run container from image:
>` docker run -d -p 9090:9090 --name=simpleflaskapidocker simpleflaskapidocker:2 `  

## Send request to API:
> ` curl localhost:9090 `  
> ` curl localhost:9090/countries `
