# Docker Combined Multiple Volumes

## Code setup:

> ` git clone https://github.com/jsandevops/docker.git `  
> ` cd docker/dockervolumes/multiplevolumes `  

## Build a docker image:  
> ` docker build -t dockervolumesmultiplevolumes:1 . `  
  
## Check images:
> ` docker image ls `  

## Check if any volume exists:
> ` docker volume ls `  

No new volume should exist

## Run container from image:
> ` docker run -d --rm -p 9090:9090 --name=dockervolumesmultiplevolumes -v /root/hostapp:/app -v appdata:/app/appdata -v /root/hostapp/countries.json  dockervolumesmultiplevolumes:1 `    

**Note:**
- Here all three types of volumes are mapped together   
- One very important concept is that, file /root/hostapp/countries.json will not be overwritten due to bind mount since Docker evaluates all the volumes that are set for a container and if there are clashes, the longer internal path wins i.e. anonymous volume in this case

## Check if any volume exists:
> ` docker volume ls `  

We would be able to see two volume, one anonymous and one named. Also host folder /root/hostapp is mapped with /app folder inside Docker container

## **Conclusion:**
- We can map multiple volumes of same or multiple types, while running a container  
- Docker evaluates all the volumes that are set for a container and if there are clashes, the longer internal path wins. So if we want a certain folder should not be overwritten while mounting bind mount then mount a anonymous volume with longer internal path to avoid overwritting  
