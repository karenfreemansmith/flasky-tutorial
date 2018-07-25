FROM python:3-alpine
MAINTAINER karenfreemansmith@gmail.com

WORKDIR /flasky
add . /flasky

RUN export http_proxy="http://webproxy.us164.corpintra.net:8080" \
    export https_proxy="http://webproxy.us164.corpintra.net:8080" \
    export ftp_proxy="http://webproxy.us164.corpintra.net:8080" \
    pip install -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "hello.py"]
