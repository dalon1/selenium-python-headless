FROM ubuntu:latest
MAINTAINER dannel

## 1. Setting up local environment
RUN apt-get update &&
    apt-get install -y git &&
    apt-get install -y curl &&
    apt-get install -y wget &&
    apt-get install -y unzip &&
    apt-get install -y python3 &&
    apt-get install -y python3-pip

## 2. Setting up chrome browser
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-get-key add &&
    echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list &&
    apt-get update &&
    apt-get install -y google-chrome-stable

## 3. Setting up chrome driver
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&
    mv chromedriver_linux64.zip &&
    unzip chromedriver_linux64.zip &&
    mv chromedriver /usr/bin/chromedriver &&
    chmod +x /usr/bin/chromedriver &&
    rm chromedriver_linux64.zip &&
    apt-get install -y libnss3


