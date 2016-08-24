FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python python-pip -y

# Download and install Flask framework:
RUN pip install flask

RUN mkdir -p /usr/local/src
COPY . /usr/local/src

WORKDIR /usr/local/src
EXPOSE 5000


CMD python /usr/local/src/run.py
