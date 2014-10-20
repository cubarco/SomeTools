# -*- coding=utf8 -*-
__author__ = 'cubelin'

import urllib2
import getpass

content_tmp = urllib2.urlopen("http://m.baidu.com/").read()

if content_tmp.find(r"192.168.50.3:8080") > 0:

    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')

    import re
    import httplib
    import urllib

    params_list = re.findall(r"href='.*?\?(.*?)'", content_tmp)
    params = 'method=login&param=true&' + params_list[0]

    data_urlencode = urllib.urlencode({"username": username,
                                       "pwd": password,
                                       "validcode": "no_check",
                                       "is_check": "true"})
    requrl = "http://192.168.50.3:8080/eportal/userV2.do?" + params
    #header必须要包含Accept-Language和User-agent，否则将无返回数据
    headerdata = {"Content-type": "application/x-www-form-urlencoded", "Accept-Language": "zh_cn",
                  "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  + "Chrome/31.0.1650.57 Safari/537.36"}
    conn = httplib.HTTPConnection("192.168.50.3:8080")
    conn.request(method="POST", url=requrl, body=data_urlencode, headers=headerdata)
    response = conn.getresponse()
    res = response.read()
    print "Successfully logged in"

elif content_tmp.find("baidu") > 0:
    print "Already Logged in"

else:
    print "An unexpected error has occurred."
