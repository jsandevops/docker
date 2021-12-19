# Docker Named Volumes

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockervolumes/named `  

## Build a docker image:  
> ` docker build -t dockervolumesnamed:1 . `  
  
## Check images:
> ` docker image ls `  

## Check if any volume exists:
> ` docker volume ls `  

No new volume should exist

## Run container from image:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesnamed -v mynamedvolume:/app dockervolumesnamed:1 `  

Note: an extra -v flag in above run command, this is used to specify a volumne

## Check if any volume exists:
> ` docker volume ls `  

Now one volume with name mynamedvolume should exist

## Send request to API:
> ` curl localhost:9090 `  
> ` curl localhost:9090/countries `  
> ` docker exec -it dockervolumesnamed cat countries.json `  
> ` curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "India", "capital": "Delhi", "area": 10003122}' http://localhost:9090/countries `  
> ` curl localhost:9090/countries `  

## Stop the container and check if container exists:
> ` docker stop dockervolumesnamed `  
> ` docker ps `  

Container should not exists anymore

## Check if any volume exists:
> ` docker volume ls `  

Yes, the volume with name *mynamedvolume* should still exist

## Run the container again with same volumn (-v option) for mynamedvolume as before:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesnamed -v mynamedvolume:/app dockervolumesnamed:1 `  
> ` curl localhost:9090/countries `  

Here we should see two countries in the output

## **Conclusion:**
- Data is  persisted even if the container is stopped, destroyed and started again  
- We can see named volume but since it is managed by Docker, we do not know the path of the volume on host machine
- If container is started with --rm flag, container will be deleted but the volume will still be there, when container is stopped  
- We can not define named volume creation in Dockerfile but while spinning a container
