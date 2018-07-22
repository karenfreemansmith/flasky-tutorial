FROM python:3-alpine
MAINTAINER karenfreemansmith@gmail.com

WORKDIR /flasky
add . /flasky

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "hello.py"]
