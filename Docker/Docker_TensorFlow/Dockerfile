# The latest-gpu-jupyter is 2.3.1, but Tensorflow will remove "latest" to actual version number in the future
FROM tensorflow/tensorflow:2.3.0-gpu-jupyter
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#CMD ["bash"]