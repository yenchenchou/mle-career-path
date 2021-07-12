# Some Github things easy to forget

## Setup multiple ssh keys

1. Go to profile -> settings -> SSH section

2. Generate a key from your local
    * `ssh-keygen -t rsa <your_email_in_repo>`

3. create config file
    * touch config
    * Host, Hostname, User, IdentityFile

    ```bash
    Host github.com
    HostName github.com
    User yenchenchou -> this is according to your github name
    /Users/<yourname_on_pc>/.ssh/
    ```

## Common git structure in BIG tech

1. individual branches -> dev branch -> test branch -> master

## Common Syntax

```bash
# basic operations
git add .
git commit -m "update"
git push origin branch

# create local branch
git checkout -b branch2

# push local created branch
git push --set-upstream origin branch2

# clone specific branch
git checkout -b branch3 origin/branch3

# pull a update from branch to existing branch
git pull origin branch4/branch4
# equal to
git fetch origin branch4  
git checkout branch4  
git merge origin/branch4  

```
