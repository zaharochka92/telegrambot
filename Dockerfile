FROM python:3

WORKDIR /telegrambot

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

COPY telegbot.py ./
COPY meduzanews.py ./
COPY exchange.py ./
COPY rssnews.py ./
COPY probki.py ./
COPY weather.py ./
COPY mikrotik.py ./
COPY aruba.py ./
COPY teletokens.py ./

CMD [ "python", "./telegbot.py" ]