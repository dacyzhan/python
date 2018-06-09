#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
三个 单引号 表示块注释
本节为 字符串和编码练习 python 中要注意代码缩进 ，缩进代表代码块
'''


def testStr():
    print('test')
    print('包含中文的str')

# ord()函数获取字符的整数表示
    print(ord('a'))
# chr()函数把编码转换为对应的字符
    print(chr(97))
# 以Unicode表示的str通过encode()方法可以编码为指定的byte
    print('ABC'.encode('ascii'))
# Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
    print(u'中文'.encode('utf-8'))

    print('abc'.decode('utf-8'))


    print('\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# 格式化数据
# 关于块注释 ''' ''' 需要注意的是 注释也必须和代码对齐
    '''格式化数据常见的占位符有：%d 整数,%f 浮点数,%s 字符串,%x 十六进制整数'''

    print('hi, %s , you have ￥%d yuan.' % ('dacy',1000))

# 对于Unicode字符串，用法完全一样，但最好确保替换的字符串也是Unicode字符串：
    print(u'Hi, %s' % u'Michael')

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
    print('Age: %s. Gender: %s' % (25, True))
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
    print('growth rate: %d %%' % 7)


if __name__=='__main__':
    testStr()