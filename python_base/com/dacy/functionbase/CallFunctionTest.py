# -*- coding:utf-8 -*-
''' 函数调用练习'''

def callfunctiontest():
    print('callfunctiontest****************')

    # abs() 取绝对值  ,参数必须为数值
    a =-100
    print(abs(a))
    b =100
    print(abs(b))
    c =0
    print(abs(c))
    # cmp(x,y) 比较函数 如果 x>y 则返回 1 ，如果 x=y 则返回 0， 如果 x<0 则返回 -1
    print(cmp(2,1))
    print(cmp(2,2))
    print(cmp(1,2))

    #数据类型转换
    print(int('123'))
    print(int(123.4))
    print(str(123))
    print(float('12.34'))
    print(unicode(100))
    print(bool(1)) # True
    print(bool(2)) # True
    print(bool(-1))  # True

    print(bool('')) #False
    print(bool(0))   #False



if __name__ =='__main__':
    callfunctiontest()