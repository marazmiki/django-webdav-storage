#!/usr/bin/env bash

set -e

# Install the WebDAV server based on "nginx"
sudo apt-add-repository -y ppa:nginx/development
sudo apt-get update
sudo apt-get install -y nginx-extras

# Drop all the default configs
sudo rm -rf /etc/nginx-sites-enabled/*

# Copy predefined WebDAV config and make sure it works
sudo cp ./.travis/nginx/webdav.conf /etc/nginx/sites-enabled/webdav.conf
sudo nginx -t && sudo service nginx reload

# And finally, create a pretty domain name for our just created WebDAV service
echo "127.0.0.1 webdav-server.com" | sudo tee -a /etc/hosts > /dev/null
