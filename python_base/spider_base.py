# -*-coding:UTF-8 -*-
import unittest
import urllib
import urlparse

def demo():
    str='http://www.baidu.com'
    s=urllib.urlopen(str);
    # list=urllib.urlopen(str).readlines();
    msg=s.info();
    # printlist(msg.headers)
    # printlist(msg.items())
    # printlist(dir(msg))
    # print(s.getcode())
    print(s.info())
def printlist(s):
    for i in s:
        print(s)

def retrieve():
    # urllib.urlretrieve('http://www.baidu.com','index.html',reporthook=progress)
    urllib.urlretrieve('http://www.qiqipu.com/dy/dzp/37643/player.html?37643-0-0','index.html',reporthook=progress)
    # printlist(fname)

def progress(blk,blk_size,total_size):
    print(total_size)
    print('%d/%d - %.02f%%' % (blk*blk_size,total_size,(float)(blk*blk_size)*100/total_size))

def urlencode():
    params = {'scode': 100,'name':'爬虫基础课程','comment':'very goog'}
    qs = urllib.urlencode(params)
    print(qs)
    print(urlparse.parse_qs(qs))

def download_stock_data():
    for sid in stock_list:
        url ='http://hq.sinajs.cn/list='+sid
        fname = sid+'.csv'
        print('down loading  %s form %s' %(fname,url))
        urllib.urlretrieve(url,fname)

if __name__ == '__main__':
    stock_list = ['sh601006','sh000001']
    download_stock_data()
