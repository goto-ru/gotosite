goto-ru/gotosite
----------------

|goto-ru| |landscape_io|

A new version of GoTo's website. Kind of a tailored CRM, based on Django.

.. |goto-ru| image:: https://img.shields.io/badge/GoTo-project-4bb89b.svg
        :target: https://github.com/goto-ru/
        :alt: GoTo project
.. |agpl-v3| image:: https://img.shields.io/badge/license-AGPLv3+-663366.svg
.. |landscape_io| image:: https://landscape.io/github/goto-ru/gotosite/master/landscape.svg?style=flat
        :target: https://landscape.io/github/goto-ru/gotosite/master
        :alt: Code Health



Setting up
==========

For development
Dependencies: python3, postgres
1. git clone https://github.com/goto-ru/gotosite/
#. cd gotosite
#. pip3 install -r requirements.txt
#. python3 manage.py migrate
#. python3 runserver

For production
Dependencies: docker, docker-compose
1. git clone https://github.com/goto-ru/gotosite/
#. docker-compose up -d --build
   Service will become available at 0.0.0.0:8001
#. (Optionally) for CI you can set up https://github.com/Omrigan/flask-github-ci

