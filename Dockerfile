FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install wget build-essential libwrap0-dev libssl-dev python python-distutils-extra libc-ares-dev uuid-dev libcurl4-openssl-dev libmysqlclient-dev python-pip -y
#RUN easy_install pip==1.2.1

# Download and install Flask framework:
RUN pip install flask

RUN mkdir -p /usr/local/src
COPY . /usr/local/src

WORKDIR /usr/local/src
EXPOSE 5000


CMD python /usr/local/src/run.py
