# install flask version 2.1.0
include python
include python::flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
