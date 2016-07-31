# bitbucket-deploy-keys
Simple python script for uploading deployment keys to bitbucket repository from command line.

Usage:
```sh
$ python bb-deploy-keys --accountname brutesque --repo_slug bitbucket-deploy-keys --user brutesque --label test ~/.ssh/id_rsa.pub
```

More info:
https://confluence.atlassian.com/bitbucket/deploy-keys-resource-296095243.html#deploy-keysResource-POSTanewkey
