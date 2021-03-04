# Some Github things easy to forget

## Setup multiple ssh keys

1. Go to profile -> settings -> SSH section

2. Generate a key from your local
    * `ssh-keygen -t rsa <your_email_in_repo>`

3. create config file
    * touch config
    * Host, Hostname, User, IdentityFile
    ```
    Host github.com
    HostName github.com
    User yenchenchou -> this is according to your github name
    /Users/<yourname_on_pc>/.ssh/
    ```

## Common git structure in BIG tech

1. individual branches -> dev branch -> test branch -> master