#!/bin/bash

DB_NAME='_default'
DB_HOST='127.0.0.1'
DB_PORT='8086'
EMAIL_SERVER='smtp.gmail.com'
EMAIL_PORT='25'
METRICS='./metrics'

. config.sh

for var in DB_{NAME,HOST,PORT}, EMAIL{,_PASSWORD,_SERVER,_PORT}, METRICS; do
	export $var
done
