# Docker Bind Mount

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockervolumes/bindmount `  

## Build a docker image:  
> ` docker build -t dockervolumesbindmount:1 . `  
  
## Check images:
> ` docker image ls `  

## Check if any volume exists:
> ` docker volume ls `  

No new volume should exist

## Make host directory and add a file:
> ` mkdir /root/hostapp `   
> ` echo '{"name": "India", "capital": "Delhi", "area": 10003122}' > /root/hostapp/countries.json `   
> ` ls /root/hostapp `   

## Run container from image:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesbindmount -v /root/hostapp/countries.json:/app/countries.json dockervolumesbindmount:1 `    

**Note:** an extra -v has path (starting by /) instead of just name. We are mapping just file here.
**Warning:** In case, when we map a host folder with container folder then the contents of the container folder will be overwriten

## Check if any volume exists:
> ` docker volume ls `  

We would not be able to see any volume but still the host file /root/hostapp/countries.json is mapped with /app/countries.json file inside Docker container.
Any changes in host file or docker container would be repliacted at both the places

## Send request to API:
> ` curl localhost:9090 `   
> ` curl localhost:9090/countries `  
> ` docker exec -it dockervolumesbindmount cat countries.json `  

## Stop the container and check if container exists:
> ` docker stop dockervolumesbindmount `     
> ` docker ps `   

Container should not exists anymore

## Add new data to hostfile:
> ` echo '[ { "area": 10003120, "capital": "Delhi", "id": 1, "name": "India" }, { "area": 10003122, "capital": "Delhi", "id": 2, "name": "India" } ]' > /root/hostapp/countries.json `   
> ` cat /root/hostapp/countries.json `   

## Run the container again with same volumn (-v option) with same host folder as before:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesbindmount -v /root/hostapp/countries.json:/app/countries.json dockervolumesbindmount:1 `     
> ` curl localhost:9090/countries `     

Here we should see two countries in the output

## **Conclusion:**
- Data is  persisted even if the container is stopped, destroyed and started again  
- When the data is changed in host file, it gets repliacted in container
- We cannot see bind mound in volumes but we know the path of the volume on host machine
- If container is started with --rm flag, container will be deleted but the host folder will still be there, when container is stopped
- We can not define bind mount creation in Dockerfile but while spinning a container
