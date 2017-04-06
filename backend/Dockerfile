FROM continuumio/anaconda3:latest

USER root

RUN apt-get update && \
    apt-get install -y \
        python3-dev \
        build-essential \
        libx11-dev && \
    apt-get clean


COPY requirements /tmp/requirements
RUN pip install -r /tmp/requirements/pip.txt

COPY src /src
WORKDIR /src