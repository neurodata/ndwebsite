#!/bin/bash

WEBSITE_IP=128.220.176.7

docker run -d \
	--volumes-from ndwebmysqldir \
	-v /var/www/neurodata.io/ndwebsite:/var/www/ndwebsite/ \
	-v /etc/ssl/private/neurodata.io:/etc/ssl/private/neurodata.io/ \
	-p $WEBSITE_IP:80:80 \
	-p $WEBSITE_IP:443:443 \
	--name ndwebsite \
	--restart=always \
	ndwebsite:ssl
