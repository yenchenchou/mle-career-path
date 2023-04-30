FROM python:3.10

ENV PIPENV_VENV_IN_PROJECT 1

RUN apt-get update && \
    apt-get install -y \
    graphviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /home/project
USER root