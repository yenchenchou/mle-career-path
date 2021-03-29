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

1. **Pod**
2. **Service**: map the port od diff pods inside the cluster and becomes a bridge for kubeproxy. The reason why `service` is important is that pod may change the ip as it is updated. Using `service` give you a better way to avoid finding the pod's ip everytime.
3. **Deployment**: maintain a set of identical pods to ensure they have the correct config and the right number of pods

| Pods | Deployment |
| ---------------------------------- | -----------------------------------------------------|
| runs single set of containers      | runs a set of identicall pods                        |
| good for one-off dev process       | monitor the state of each pod, updating as necessary |
| rarely used directly in production | good for production                                  |

## Differences between Docker compose and Kubernetes

| Docker Compose | Kubernetes |
|-|-|
| Each entry can get docker-compose to build image| K8S expects all images to already be built -> make sure the image is hosted on hub|
| Each entry in `services` represents a contqiner | One config file per pbject we want to create -> make one config file to make pods|
| Each entry defines the networking (ports) | Manual set up is needed -> set a config file for networking|

### Important notes

1. We only work with the master in the K8S cluster. But of course you can still access manually such as using Docker.
2. K8s don't build image
3. The master decide which node to run the container by default
4. We update the desired config file to the master so that we can control K8S
5. The master will run consistantly
6. Use Declarative approach as possible instead of imerative approach unless neccesary
7. The `name` and `kind` together are a unique identifier to help K8S to find the existing object/pod and update it instead of creating an entire new one
8. According to K8S, things like num containers, name, port are not editable. Update by using the image is the only way. So we need to use `deployment`
9. The reason we sometims mess up with docker inside the pod: clean the cache or debug. You may either use `kubectl` or `docker`.

## Usage

1. update image but does not touch anything from deployment.yaml `Deployment`:

    `kubectl set image object_type/object_name container_name=new_image_to_use`

    For exmaple:

    `kubectl set image deployment/client-deployment client=stephengrider/multi-client:v5`

## Volume

1. In K8s, the definition of "volume" is different than usual. It means an object that allows a container to store data at the pod level.

2. Even having a volume in the same pod can avoid db crash but what if the pod carashes? So, we come up with other types of volume:
    * persistent volume claim: dynamic options for you to choose but will only used when actually needed -> claim config files
    * persistent volume: the volume that exists outside the pods, this will last for long time.
