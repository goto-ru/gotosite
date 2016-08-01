FROM python:3.5
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /root/app/requirements.txt
WORKDIR /root/app
RUN pip install -r /root/app/requirements.txt
ENV ENV=production
CMD ./startup.sh
