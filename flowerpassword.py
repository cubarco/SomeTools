# -*- coding=utf8 -*-
__author__ = 'cubelin'

import hmac
import argparse


def getpassword(password, key):
    md5one = hmac.new(key, msg=password).hexdigest()
    md5two = hmac.new('snow', msg=md5one).hexdigest()
    md5three = hmac.new('kise', msg=md5one).hexdigest()

    rule = list(md5three)
    source = list(md5two)
    temp = 'sunlovesnow1990090127xykab'

    for i in range(32):
        try:
            int(source[i])
        except ValueError:
            if rule[i] in temp:
                source[i] = source[i].upper()

    code32 = ''.join(source)
    code1 = code32[0]

    try:
        int(code1)
    except ValueError:
        code16 = code32[:16]
    else:
        code16 = 'K' + code32[1:16]

    print code16

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='%(prog)s [-p PASSWORD] -k <KEY>',
                                     description=
                                     '有别于一般密码管理方式，“花密”是一种可记忆、非储存的密码管理方案，'
                                     '你只需记住一个“记忆密码”加上“区分代号”就可以使用“花密”为不同的账号生成'
                                     '难以破解的强壮密码。')
    parser.add_argument('-k', action='store', default=None, nargs=1, dest='key')
    parser.add_argument('-p', action='store', default=None, nargs='?', dest='password')
    args = parser.parse_args()

    try:
        key = args.key[0]
    except TypeError:
        parser.print_help()
        exit(1)

    password = args.password
    if not password:
        import getpass
        password = getpass.getpass('Password: ')

    getpassword(password, key)