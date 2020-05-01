FROM alpine:latest

LABEL Maintainer="Muhammed Iqbal <iquzart@hotmail.com>"

RUN apk add --no-cache --update python3
    

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]