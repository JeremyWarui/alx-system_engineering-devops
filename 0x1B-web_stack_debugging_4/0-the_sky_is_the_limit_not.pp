# fix nginx request limit using puppet

exec { 'modify ulimit and restart nginx':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
