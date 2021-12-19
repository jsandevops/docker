# Docker Anonymous Volumes

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockervolumes/anonymous `  

## Build a docker image:  
> ` docker build -t dockervolumesanonymous:1 . `  
  
## Check images:
> ` docker image ls `  

## Check if any volume exists:
> ` docker volume ls `  

No new volume should exist

## Run container from image:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesanonymous dockervolumesanonymous:1 `  

Note: --rm flag will remove the container once stopped and will also delete volume at the same time

## Check if any volume exists:
> ` docker volume ls `  

Now one anonymous volume should exist

## Send request to API:
> ` curl localhost:9090 `  
> ` curl localhost:9090/countries `  
> ` docker exec -it dockervolumesanonymous cat countries.json `  
> ` curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "India", "capital": "Delhi", "area": 10003122}' http://localhost:9090/countries `  
> ` curl localhost:9090/countries `  

## Stop the container and check if container exists:
> ` docker stop dockervolumesanonymous `  
> ` docker ps `  

Container should not exists anymore

## Check if any volume exists:
> ` docker volume ls `  

Newly created volume should not exist anymore

## Run the container again:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesanonymous dockervolumesanonymous:1 `  
> ` curl localhost:9090/countries `  

Here we should see only one country in the output

## **Conclusion:**
- Data does not persisted if the container is stopped and created again  
- If container is started with --rm flag, both anonymous volume and container will be deleted when container is stopped  
- If container is started without --rm flag, anonymous volume will persist and data can be retained when container is stopped and started again
- We can define anonymous volume creation in Dockerfile OR while spinning a container
