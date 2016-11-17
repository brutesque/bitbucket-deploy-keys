# bitbucket-deploy-keys
Simple python script for uploading deployment keys to bitbucket repository from command line.

Usage:
```sh
$ python bb-deploy-keys.py --help
```
```sh
usage: bb-deploy-key.py [-h] -a ACCOUNTNAME -r REPO_SLUG -u USER [-l LABEL]
                        file

Add deployment key to bitbucket repository.

positional arguments:
  file                  The file containing the public key. (Eg.:
                        ~/.ssh/id_rsa.pub)

optional arguments:
  -h, --help            show this help message and exit
  -a ACCOUNTNAME, --accountname ACCOUNTNAME
                        The team or individual account.
  -r REPO_SLUG, --repo_slug REPO_SLUG
                        The repo identifier (not to be confused with the
                        repo's name).
  -u USER, --user USER  Your bitbucket username.
  -l LABEL, --label LABEL
                        A display name for the key.
```

Example:
```sh
$ wget https://raw.githubusercontent.com/brutesque/bitbucket-deploy-keys/master/bb-deploy-key.py
$ ssh-keygen -b 4096 -f ~/.ssh/id_rsa -C $USER@$(uname -n) -t rsa -N '' -q
$ python bb-deploy-key.py -a [accountname] -r [repo_slug] -u [username] -l "$USER@$(uname -n)" ~/.ssh/id_rsa.pub
```

More info:
https://confluence.atlassian.com/bitbucket/deploy-keys-resource-296095243.html#deploy-keysResource-POSTanewkey
