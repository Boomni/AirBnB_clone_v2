#!/usr/bin/env bash
#Sets up my web servers for the deployment of web_static

if [ ! -x "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

if [ -d "/data/web_static/current" ]; then
    sudo rm -rf /data/web_static/current;
fi

sudo echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/index.html /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i 's#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n#g' /etc/nginx/sites-available/default

sudo service nginx restart
