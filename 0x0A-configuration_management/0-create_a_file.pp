# Using Puppet, create a file in /tmp.

file { '/tmp/school':
    ensure  => file,
    path    => '/tmp/school',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
    content => 'I love Puppet'
}
