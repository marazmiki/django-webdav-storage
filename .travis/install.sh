#!/usr/bin/env bash

set -e

# Install the WebDAV server based on "nginx"
sudo apt-add-repository -y ppa:nginx/development
sudo apt-get update
sudo apt-get install -y nginx-extras

echo "127.0.0.1	webdav-server.com" | sudo tee -a /etc/hosts >/dev/null

sudo cp ./tests/.configs/nginx/nginx.conf    /etc/nginx/nginx.conf
sudo cp ./tests/.configs/nginx/webdav.conf   /etc/nginx/webdav.conf

sudo nginx -t
sudo service nginx restart
