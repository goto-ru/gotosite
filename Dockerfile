FROM ubuntu:16.04
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip nginx
RUN apt-get install -y libpq-dev python3-dev
WORKDIR /root/app
ADD requirements.txt /root/app/requirements.txt
RUN pip3 install -r /root/app/requirements.txt
ADD . /root/app
RUN python3 manage.py collectstatic --noinput
ADD mainsite.conf /etc/nginx/sites-enabled
ADD nginx.conf /etc/nginx
ENV ENV=production
CMD ./startup.sh
