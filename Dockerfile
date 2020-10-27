FROM python:3.8-alpine
RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            mariadb-dev \
            build-base \
            linux-headers \
            pcre-dev \
            bash

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ENV PATH /flask/lib:/flask/lib/bin:$PATH
ENV PYTHONPATH /flask/lib:/flask/lib/bin:$PYTHONPATH