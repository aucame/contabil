#!/bin/bash

# scp -r /usr/share/nginx/html/contabil/bower_components root@200.98.174.103:/usr/share/nginx/html/contabil
# scp *.* root@200.98.174.103:/usr/share/nginx/html/contabil

# Deploy App
# scp -r app/*.js root@200.98.174.103:/usr/share/nginx/html/contabil/app

# Deploy backend-api
# scp -r backend/api root@200.98.174.103:/usr/share/nginx/html/contabil/backend

# Deploy BackEnd
# cd backend
# scp *.py *.php *.xls *.pdf *.html *.json *.sql *.txt   root@200.98.174.103:/usr/share/nginx/html/contabil/backend
# cd ..

# Deploy HTML
# scp *.html *.png *.json *.txt *.css *.sh  root@200.98.174.103:/usr/share/nginx/html/contabil

# Deploy Producao
cd app
scp appConfig.js root@200.98.174.103:/usr/share/nginx/html/contabil/app
cd ..
cd backend/api/configuration/properties
scp contabil.properties root@200.98.174.103:/usr/share/nginx/html/contabil/backend/api/configuration/properties
cd /usr/share/nginx/html/contabil
