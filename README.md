# bitbucket-deploy-keys
Simple python script for uploading deployment keys to bitbucket repository from command line.

Usage:
```sh
$ python bb-deploy-keys.py --help
```

Example:
```sh
$ wget https://raw.githubusercontent.com/brutesque/bitbucket-deploy-keys/master/bb-deploy-key.py
$ ssh-keygen -b 4096 -f ~/.ssh/id_rsa -C $USER@$(uname -n) -t rsa -N '' -q
$ python bb-deploy-keys.py -a [accountname] -r [repo_slug] -u [username] -l "$USER@$(uname -n)" ~/.ssh/id_rsa.pub
```

More info:
https://confluence.atlassian.com/bitbucket/deploy-keys-resource-296095243.html#deploy-keysResource-POSTanewkey
