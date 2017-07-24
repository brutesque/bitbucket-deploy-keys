#!/usr/bin/env python
import argparse
import requests
import os
import getpass

parser = argparse.ArgumentParser(description='Add deployment key to bitbucket repository.')

parser.add_argument('-a', '--accountname',
    help='The team or individual account.', type=str, required=True)

parser.add_argument('-r', '--repo_slug', type=str, required=True,
    help="The repo identifier (not to be confused with the repo's name).")

parser.add_argument('-u', '--user', type=str, required=True,
    help='Your bitbucket username.')

parser.add_argument('-l', '--label', type=str,
    help='A display name for the key.')

parser.add_argument('file',
    help='The file containing the public key. (Eg.: ~/.ssh/id_rsa.pub)')

parser.add_argument('-p', '--password',
    help='Supply password (insecure, use $BITBUCKET_PASSWORD)',
    default=os.environ.get('BITBUCKET_PASSWORD'))

args = parser.parse_args()
password = args.password if args.password else getpass.getpass()

response = requests.request(
    method='POST',
    url=('https://api.bitbucket.org/1.0/repositories/%s/%s/deploy-keys' % (args.accountname, args.repo_slug)),
    data={
        'key': open(os.path.expanduser(args.file)).read(),
        'label': args.label,
    },
    auth=(args.user, password),
)

if response.status_code == 200:
    print('success')
elif response.status_code == 400:
    print('Someone has already registered this key as a deploy key for this repository')
elif response.status_code == 401:
    exit('incorrect credentials')
else:
    print(response.status_code)
    print(response.content)
    exit('failed')
