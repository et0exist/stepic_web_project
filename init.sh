#!/bin/bash
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#gunicorn -c /home/box/web/etc/gunicorn_wsgi.conf hello:wsgi_application
gunicorn -c /home/box/web/etc/gunicorn_django.conf ask.wsgi:application
#sudo /etc/init.d/mysql start
#mysql -u root -e "CREATE DATABASE qa"
