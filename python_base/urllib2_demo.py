#-*- coding: utf-8 -*-
import urllib2
import urllib

def urlopen():
    url= 'http://www.baidu.com'
    try:
        s= urllib2.urlopen(url,timeout=3)
    except urllib2.HTTPError, e:
        print(e)
    else:
        print(s.read(100))
        s.close()

def request():
    # 定制 HTTP 头
    headers ={'User=Agent':'Mozilla/5.0','x-my-header':'my value'}
    req= urllib2.Request('http://www.baidu.com',headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    print(req.headers)
    s.close()

def request_post_debug():
    # POST
    data ={'username':'kamibox','password':'xxxxx'}
    #headers ={'User=Agent':'Mozilla/5.0','x-my-header':'my value'}
    headers = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request('http://www.douban.com' ,data=urllib.urlencode(data),headers = headers )
    opener  = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))

def test():
    print('aaa')

if __name__ == '__main__':
    test()