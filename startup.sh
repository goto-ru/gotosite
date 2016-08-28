python3 manage.py migrate
service nginx start
uwsgi --socket socket.sock --wsgi-file gotosite2/wsgi.py
