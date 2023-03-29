# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "48i \x22\\\tlocation /redirect_me {\n\t\t return 301 https:\/\/google.com;\n\t}\n\x22" /etc/nginx/sites-available/default ; sudo service nginx restart',
}
