# File System

## Basics

### Directory & Description

##

## 1. Environment

### Check which shell are supported  

`cat /etc/shells`

### Tell what kind of interpreter to run

`#! /bin/zsh` or `#! /bin/bash` ...etc

## 2. Variables

### `read` take input from keyboard and save into variable(s)

```
touch hello.sh
read -p 'username: ' user_var
# -sp is without showing the value you entered
read -sp "password: " user_password
echo
echo "Your favorite food "
read -a foods
echo "Your username is" $user_var
echo "Your password is" $user_password
echo "Your food are ${foods[0]}, ${foods[1]}"
```

3. `stdin`, `stderr`, `stdout`

- [What Are stdin, stdout, and stderr on Linux?](https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/)
