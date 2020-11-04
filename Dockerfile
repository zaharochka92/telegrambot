FROM ubuntu:18.04

WORKDIR /telegrambot
RUN apt update 
RUN apt install -y python3 python3-pip firefox

COPY req.txt ./
RUN pip3 install --no-cache-dir -r req.txt

COPY telegbot.py ./
COPY meduzanews.py ./
COPY exchange.py ./
COPY rssnews.py ./
COPY probki.py ./
COPY weather.py ./
COPY mikrotik.py ./
COPY aruba.py ./
COPY teletokens.py ./
COPY firefox-geckodriver_82.0+build2-0ubuntu0.18.04.1_amd64.deb ./

RUN dpkg -i firefox-geckodriver_82.0+build2-0ubuntu0.18.04.1_amd64.deb

CMD [ "python", "./telegbot.py" ]
