#Config client ssh file to conect to server without password
“` file_line { 'holberton':

path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'PasswordAuthentication':

path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
} “`
