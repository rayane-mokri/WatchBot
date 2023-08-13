FROM python:3.10

RUN apt-get update && apt-get upgrade -y

WORKDIR /bot

COPY Bots /bot
COPY envs /envs

RUN pip install -r requirements.txt

RUN python scripts/reddit.py

RUN python main.py