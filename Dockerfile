FROM ubuntu:16.04
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python3 python3-dev python3-pip python python-pip python-dev
RUN apt-get install -y nodejs npm
RUN apt-get install -y libpq-dev
RUN apt-get build-dep -y python-imaging
RUN apt-get install -y libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
RUN pip3 install --upgrade pip
RUN ln -s /usr/bin/nodejs /usr/bin/node
EXPOSE 8000
RUN npm install bower -g
ADD . /root/app
RUN pip3 install -r /root/app/requirements.txt --upgrade
WORKDIR /root/app/goto/static
RUN bower install --allow-root
WORKDIR /root/app
ENV ENV=production
CMD python3 manage.py migrate; gunicorn gotosite2.wsgi -b 0.0.0.0:8000
