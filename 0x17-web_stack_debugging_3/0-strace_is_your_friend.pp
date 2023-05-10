#puppet script to rectify the error from server

exec {'fix server':
  command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  provider => shell,
  path     => '/usr/bin:/bin',
}
