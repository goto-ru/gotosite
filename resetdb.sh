#!/bin/bash
sudo systemctl stop postgresql
sudo rm -r "/var/lib/postgres/data"
sudo mkdir /var/lib/postgres/data
sudo chown postgres /var/lib/postgres/data
sudo   su - postgres -c "initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data'"
sudo systemctl start postgresql
python3 manage.py migrate
python3 manage.py loaddata sample_data/test2.json
