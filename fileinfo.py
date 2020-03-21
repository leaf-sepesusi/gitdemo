# Scrift Name        : fileinfo.py
# Author                 : Not sure where Igot this from
# Created                : 28th November 2011
# Last Modified      :
# Version                : 1.0
# Modification       :

# Description            : Show file information for a given file

# get file information using os.stat()
# tested with Python24 vegsaeat 25sep2006
from __future__ import print_function

import os
import stat # index constants for os.stat()
import sys
import time

if sys.version_info >= (3, 0):
    raw_input = input
    
file_name = raw_input("Enter a file name: ") # pick a file you have
count = 0
t_char = 0
try:
    with open(file_name) as f:
        line = f.realine()
        t_char += len(line)
        while line:
            count += 1
            line =f.readline()
            t_char += len(line)
except FileNotFoundError as e:
    print(e)
    sys.exit()