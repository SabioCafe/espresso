FROM python:3.8-alpine
RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            mariadb-dev \
            build-base \
            linux-headers \
            pcre-dev \
            bash

ENV PATH /app/lib:/app/lib/bin:$PATH
ENV PYTHONPATH /app/lib:/app/lib/bin:$PYTHONPATH