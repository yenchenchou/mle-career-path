FROM python:3.8.3

USER root

RUN apt-get update && \
    apt-get install -y \
    nano \
    git \
    vim \
    libaio1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ~/.ssh ~/.ssh
# COPY requirements.txt .

# RUN pip install -r requirements.txt
# RUN rm requirements.txt