# Fix security limits

exec { 'fix first limit' :
  command  => 'sed -i "s/nofile 5/nofile 1000000/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'fix second limit':
  command  => 'sed -i "s/nofile 4/nofile 1000000/" /etc/security/limits.conf',
  provider => shell,
}
