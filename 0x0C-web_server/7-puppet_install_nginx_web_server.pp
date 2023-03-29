# install nginx server in our server
# add redirect page
# add not found error page

#update
exec { 'apt-update':
  command => 'apt-get -y update'
}

#install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update']
}

#write on file default "hello world"
file { 'var/www/html/index.nginx-debian.html':
  ensure  => file,
  path    => 'var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}

#write on custom 404 
file { '/usr/share/nginx/html/custom_404.html':
  ensure  => file,
  path    => '/usr/share/nginx/html/custom_404.html',
  content => "Ceci n'est pas une page"
}


#config nginx 
#redirect
#custom 404
$server_str = "
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

  server_name _;

  location / {
		try_files $uri $uri/ =404;
  }

	location /redirect_me {
		return 301 https://google.com;
	}

	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /usr/share/nginx/html;
		internal;
	}

}
"
#write config on default nginx
exec { 'printf':
  command  => 'printf "%s\n" $server_str > /etc/nginx/sites-available/default'
}

exec { 'service':
  command  => 'sudo service nginx restart'
}
