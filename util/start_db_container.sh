#!/bin/bash

# create a data volume for the db container 
docker create -v /var/lib/mysql --name ndwebmysqldir ndwebsite:prod /bin/true
