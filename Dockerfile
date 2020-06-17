FROM python:3.7-alpine

LABEL Maintainer="Muhammed Iqbal <iquzart@hotmail.com>"

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
