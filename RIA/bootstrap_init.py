#!/usr/bin/python
# coding: utf-8
import subprocess, sys
import argparse

def main(argv):

    default_env = "dev"

    parser = argparse.ArgumentParser(description='Process environment.')
    parser.add_argument('env', default = default_env)
    arguments = parser.parse_args()

    virtualenv = ['virtualenv', '.', '--no-setuptools']
    print "- Creation of the virtualenv: ",
    print
    if subprocess.check_call(virtualenv):
        return 2

    bootstrap = ['bin/python', 'bootstrap.py','-c','buildout.%s.cfg' % (arguments.env)]

    print "- Bootstrap: "
    print
    if subprocess.check_call(bootstrap):
        return 3

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
