#!/usr/bin/env python

from contextlib import contextmanager
import os
import os.path
import subprocess
import sys

repos = {
    "services/gateway": "https://github.com/tuanda831/api-gateway.git",
    "services/inventory": "https://github.com/tuanda831/inventory-service.git",
    "services/search": "https://github.com/tuanda831/search-service.git",
}

# Helpers

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def bold(text):
    return "\033[1m" + text + "\033[0m"

def checkout_missing_service():
    for name, url in repos.items():
        if not os.path.exists(name):
            subprocess.call(["git", "clone", url, name])

def checkout_repo(name, url):
    if not os.path.exists(name):
        subprocess.call(["git", "clone", url, name])
        return

    print bold("Updating " + name)
    with cd(name):
        subprocess.call(["git", "checkout", "master"])
        subprocess.call(["git", "pull"])

# Commands

def checkout_master():
    for name, url in repos.items():
        checkout_repo(name, url)

def all_git_status():
    for name in repos:
        print bold("Repo: " + name)
        with cd(name):
            subprocess.call(["git", "status"])
            print ""

def main():
    if len(sys.argv[1:]) == 0:
        return checkout_master()

    if sys.argv[1] == "status":
        return all_git_status()

    if sys.argv[1] == "checkout_missing_service":
        return checkout_missing_service()

if __name__ == "__main__":
    main()
