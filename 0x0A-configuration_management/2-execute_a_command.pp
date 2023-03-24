# manifest that kills a process named killmenow

exec { 'pkill killmenow':
    command  => 'pkill killmenow',
    path     => '/usr/bin/',
    provider => shell,
    returns  => [0, 1]
}
