#!/bin/bash

docker run -d \
	--volumes-from ndwebmysqldir \
	-v /var/www/neurodata.io/ndwebsite:/var/www/ndwebsite/ \
	-p 128.220.176.10:80:80 \
	--name ndwebsite \
	--restart=always \
	ndwebsite:prod 
