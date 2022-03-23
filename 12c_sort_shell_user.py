"""
For an added challenge, after displaying each shell, also show the usernames (sorted alphabetically) who use each of those shells.
"""
from collections import defaultdict
from pprint import pprint


def shells_and_users_by_popularit(filename):
    shells = defaultdict(list)
    for line in open(filename):
        if line.startswith(("#","\n")):
            continue
        username, *rest, shell = line.strip().split(":")
        shells[shell].append(username)
    return sorted(shells.items(), key=len)

pprint(shells_and_users_by_popularit('/etc/passwd'))


