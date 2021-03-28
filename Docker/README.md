# Docker Operation Syntax Memo
**Here includes some syntax that not mentioned on Docker official website**

## Handling images
#### Check images by name
**No need to specify the entire name as long as it meets you requirements**
1. grep: `docker images | grep <imagename>`
2. by regex: 

#### remove images by name
1. docker rmi -f $(docker images | grep <imagename>)

## Handling containers
#### Check containers by name
1. grep: `docker container ps -a | grep yc`
2. filter: `docker container ps -a --filter ancestor="yc/tf_jupyter_image:v2"`

#### remove containers by name
1. `docker container rm $(docker container ps -a | grep yc_explore)`
2. `docker rm <container_ID>`

#### remove dangling containers with filter
Docker image prune only cleans up dangling images. A dangling image is one that is not tagged and is not referenced 
by any container.


## Some basic concept
#### Purpose of docker compose and docker compose cli
1. separate docker cli that gets installed along with Docker
2. Run multiple containers at the same time -> Docker compose create a network automatically for the containers inside 
the docker compose file (.yml) 
3. Automate some complex arguments passing the `docker run`


# 2. Kubernetes

## Def

1. What is Kubernetes?:

    portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.

2. Kubernete cluster:

    A Kubernete cluster is consist of a master node and 1 or more nodes where each node is a virtual machine or physicla computer. Each node contains one or more containers. We control the cluster by controling the cluster.

## Components of Kubernetes

## Differences between Docker compose and Kubernetes

| Docker Compose | Kubernetes |
|-|-|
| Each entry can get docker-compose to build image| K8S expects all images to already be built -> make sure the image is hosted on hub|
| Each entry in `services` represents a contqiner | One config file per pbject we want to create -> make one config file to make pods|
| Each entry defines the networking (ports) | Manual set up is needed -> set a config file for networking|