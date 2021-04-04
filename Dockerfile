FROM python:3.9-alpine3.12

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV PYTHONPATH "."

RUN echo $PYTHONPATH

CMD ["/bin/sh"]