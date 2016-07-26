# goto-ru/gotosite


![GoTo project] ![Code Health]

A new version of GoTo’s website. Kind of a tailored CRM, based on Django.

# Setting up

Dependencies: python3, postgres

1.  `git clone <https://github.com/goto-ru/gotosite/>`
2.  `cd gotosite`
3.  `git submodule init`
4.  `git submodule update`
5.  `pip3 install -r requirements.txt`
6.  Here you need to run docker with postgres (sudo docker run -p 5432:5432 postgres) Don’t forget to run docker background.
7.  `python3 manage.py migrate`
8.  `python3 manage.py loaddata sample\_data/sample\_data\_1.json`
9.  `python3 manage.py runserver`

### For production

Dependencies: docker, docker-compose

1.  `git clone <https://github.com/goto-ru/gotosite/>`
2.  `cd gotosite`
3.  `git submodule init`
4.  `git submodule update`
5.  `docker-compose up -d –build`
6.  `docker-compose exec web python3 manage.py loaddata sample\_data/sample\_data\_1.json`
  **Service will become available at 0.0.0.0:8001**
7.  (Optionally) for CI you can set up <https://github.com/Omrigan/flask-github-ci>

[GoTo project]: https://img.shields.io/badge/GoTo-project-4bb89b.svg
[![GoTo project]]: https://github.com/goto-ru/
[Code Health]: https://landscape.io/github/goto-ru/gotosite/master/landscape.svg?style=flat
[![Code Health]]: https://landscape.io/github/goto-ru/gotosite/master

