FROM python:3.7-alpine

MAINTAINER Kush Shah "kush.shah999@gmail.com"

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]