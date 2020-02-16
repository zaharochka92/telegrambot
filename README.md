# telegrambot

docker build -t telebot-docker .

docker run -it -P  --rm --name telebot-docker telebot-docker

docker attach telebot-docker
