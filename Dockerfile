FROM python:3.10.13

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && \
    apt-get install -y \
    nano \ 
    vim \
    graphviz \
    git \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://install.python-poetry.org | python3 -    

WORKDIR /home/ml
USER root
ENTRYPOINT [ "/bin/bash" ]
