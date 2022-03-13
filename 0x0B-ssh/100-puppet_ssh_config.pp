#configure SSH configuration file to our needs so that you can connect to a server without typing a password
file { '~/.ssh/school':
  'PasswordAuthentication' => 'no',
}

