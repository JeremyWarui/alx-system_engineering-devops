## 0x17. Web stack debugging #3

> Project focusing on Wordpress webstack and debug to know the reason as to why it shows server error

### TASK

**0. Strace is your friend**

Using strace, find out why Apache is returning a 500 error.\
Once you find the issue, fix it and then automate it using Puppet\
(instead of using Bash as you were previously doing).

Hint:

- strace can attach to a current running process

- You can use tmux to run strace in one window and curl in another one
