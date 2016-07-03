FROM python:3.5
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
ADD requirements.txt /root/app
WORKDIR /root/app
RUN pip3 install -r /root/app/requirements.txt --upgrade
ENV ENV=production2
CMD python3 manage.py migrate; gunicorn gotosite2.wsgi -b 0.0.0.0:8000
