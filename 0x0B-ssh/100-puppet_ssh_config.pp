#Config client ssh file to conect to server without password
file_line { 'ssh_config':

path => '/etc/ssh/ssh_config',
line => 'Include /etc/ssh/ssh_config',
}

file_line { 'Host':

path => '/etc/ssh/ssh_config',
line => 'Host *',
}

file_line { 'holberton':

path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'PasswordAuthentication':

path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}
file_line { 'HashKnownHosts':

path => '/etc/ssh/ssh_config',
line => 'HashKnownHosts yes',
}
file_line { 'HashKnownHosts':

path => '/etc/ssh/ssh_config',
line => 'GSSAPIAuthentication yes',
}
file_line { 'SendEnv':

path => '/etc/ssh/ssh_config',
line => 'SendEnv LANG LC_*',
}
