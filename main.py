#!/usr/bin/env python3.9
from subprocess import call
import os
print('Hello user.')
cwd = os.getcwd()
os.chdir(cwd + '/Services')

command = input("Enter command: ")

call(["python" , "main.py" , "find_and_run_plugins" , command])
