# -*- coding:utf-8 -*-
import math
'''
定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。

'''

def test():
    print('test')
    a=my_abs(40)
    print(a)
    b=my_abs(-40)
    print(b)
    c=my_abs(0)
    print(c)

# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
# 就可以先放一个pass，让代码能运行起来。
def nop():
    pass

def testnop():
    x= 10
    if x>5:
        nop()

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def power(x):
    return x*x
def powers(x,n):
    s=1
    if x<>0 & n>0:
        while n>0:
            s=s*x
            n=n-1
        print('000')
        return s
    elif x==0:
        print('111')
        return 0
    elif n==0:
        print('222')
        return 1
    else:return '数据异常'

if __name__=='__main__':
    testnop()

    x,y= move(100,100,60,math.pi/6)
    print(x,y)
    print power(4)
    print(powers(3,3))