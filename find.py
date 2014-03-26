#!/usr/bin/env python

# -*- coding=utf8 -*-
__author__ = 'cubelin'

import os
import re


def main(parse_args):

    dir_name = parse_args.dir_name
    file_regx = parse_args.file_regx
    if dir_name[-1] == r'/':
        dir_name = dir_name[:-1]

    if parse_args.cmd:
        for root, dirs, files in os.walk(dir_name):
            if re.search(file_regx, root):
                path = root + os.path.sep
                os.system(parse_args.cmd + ' ' + path)
            for file_name in files:
                if re.search(file_regx, file_name):
                    path = root + os.path.sep + file_name
                    os.system(parse_args.cmd + ' ' + path)
    else:
        for root, dirs, files in os.walk(dir_name):
            if re.search(file_regx, root):
                path = root + os.path.sep
                print path
            for file_name in files:
                if re.search(file_regx, file_name):
                    path = root + os.path.sep + file_name
                    print path



if __name__ == "__main__":

    import argparse

    parse = argparse.ArgumentParser(usage='find.py [-h] dir_name [file_regx] [--exec CMD]',
                                    description=
                                    'Find all files whose name matches the file_regx. If file_regx is not provided it '
                                    'will automatically matches all the files in provided dir_name. If option exec is'
                                    ' provided, matched file paths will be passed to the command and be executed.'
                                    )

    parse.add_argument('dir_name', action='store')
    parse.add_argument('file_regx', action='store', nargs='?', default=r'.')
    parse.add_argument('--exec', action='store', dest='cmd')

    main(parse.parse_args())