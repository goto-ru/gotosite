FROM python:3.5
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /root/app/requirements.txt
WORKDIR /root/app
RUN pip install -r /root/app/requirements.txt
ENV ENV=production2
#CMD gunicorn gotosite2.wsgi -b 0.0.0.0:8000
CMD python3 manage.py runserver 0.0.0.0:8000
