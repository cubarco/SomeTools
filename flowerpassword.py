# -*- coding=utf8 -*-
__author__ = 'cubelin'

import sys
import hmac

password, key = '', ''
try:
    password = sys.argv[1]
    key = sys.argv[2]
except IndexError:
    print "Not enough arguments."
    exit(1)

md5one = hmac.new(key, msg=password).hexdigest()
md5two = hmac.new('snow', msg=md5one).hexdigest()
md5three = hmac.new('kise', msg=md5one).hexdigest()

rule = list(md5three)
source = list(md5two)
temp = "sunlovesnow1990090127xykab"

for i in range(32):
    try:
        int(source[i])
    except ValueError:
        if temp.find(rule[i]) > -1:
            source[i] = source[i].upper()

code32 = ''.join(source)
code1 = code32[:2]

try:
    int(code1)
except ValueError:
    code16 = code32[:16]
else:
    code16 = "K" + code32[1:16]

print code16