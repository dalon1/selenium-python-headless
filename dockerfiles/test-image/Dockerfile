FROM selenium/standalone-chrome:latest
MAINTAINER dannel
USER root
WORKDIR /qa-app
COPY requirements.txt .
COPY test test
RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && pip3 install -r requirements.txt
CMD ["python3", "-m", "unittest", "discover", "-s", "test"]