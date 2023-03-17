#! /bin/bash

apt update
apt  install fio -y
apt install nodejs -y
apt install nmp -y
apt install docker.io -y
npm install -g @angular/cli
pip3 install fastapi
pip3 install fastapi-utils
pip3 install uvicorn
pip3 install sqlalchemy
pip3 install pymysql

systemctl start docker
systemctl enable docker

cd webapp/frontend/
npm install

ng server --host <machine-ip> --port 4200

cd ../../boost-core/
uvicorn main:app --reload --host <machine-ip>
