#!/usr/bin/python

"""
Script get all repositories from github of a user
"""

import requests
import argparse


def get_repos(username):
    url = "https://api.github.com/users/%s/repos" % username
    r = requests.get(url)
    if r.ok:
        return [i['name'] for i in r.json()]
    else:
        return None


def main():
    desc = "Get all repositories of a user name from Github"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('username', help='User name for Github')
    args = parser.parse_args()

    repos = get_repos(args.username)
    if repos is not None:
        if repos:
            for repo in repos:
                print repo
        else:
            print 'This user does not have any repository.'
    else:
        print 'User does not exist.'


if __name__ == '__main__':
    main()
