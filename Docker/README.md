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
2. 

#### remove dangling containers with filter
Docker image prune only cleans up dangling images. A dangling image is one that is not tagged and is not referenced 
by any container.

