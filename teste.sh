#!/bin/bash

#scp -r /usr/share/nginx/html/contabil/bower_components root@200.98.174.103:/usr/share/nginx/html/contabil
#scp -r backend/api root@200.98.174.103:/usr/share/nginx/html/contabil/backend
scp *.html *.png *.js *.css root@200.98.174.103:/usr/share/nginx/html/contabil
