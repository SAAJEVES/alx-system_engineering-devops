# Using Puppet, install flask from pip3

package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => 'latest',
  provider => 'pip3',
}
