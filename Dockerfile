FROM python:3.5
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /root/app
WORKDIR /root/app
RUN pip install -r /root/app/requirements.txt
ENV ENV=production2
CMD python3 manage.py migrate; gunicorn gotosite2.wsgi -b 0.0.0.0:8000
