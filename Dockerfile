FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir atomic_habits

WORKDIR atomic_habits

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .


RUN chmod a+x docker/*.sh
