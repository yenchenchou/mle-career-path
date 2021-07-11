# Setup GPU Tensorflow + Jupyter through Docker 

## Single Docker file version

1. Create Dockerfile
2. Create requirements.txt
3. Build Docker image with custom tag
    
    `docker build -t <repo_name>:{tag_name} .`
    
    Example:
    
    `docker build -t yc/tf_jupyter_image:v1 .`

4. Start the container using the image, refer to [TensorFlow website](https://www.tensorflow.org/install/docker)

    * Just bash
    
    `docker run --gpus all -it 1007/tf_jupyter_image:v1 bash`
    
    * Notebook

    `docker run --gpus all -it -p 8888:8888 1007/tf_jupyter_image:v1`
    
 5. Open another terminal 
 
    * check container IP first
     
    `docker inspect <containerID> --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'`
 
    * log to server
    
    `ssh -N -f -L localhost:8888:<dockerIP>:8890 <yourusername>@10.42.162.210`