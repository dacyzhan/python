# -*- coding:utf-8 -*-
'''
此节主要是练习递归函数相关的知识

'''

def test():
    print('test ...')

def fact(x):
    if x==1:
        return 1
    else:return x*fact(x-1)

def fact_iter(n,s):
    if n==1:
        return s
    else :return fact_iter(n-1,n*s)

def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)



if __name__=='__main__':
    # test()
    print(fact_iter(5,1))
    move(4,'a','b','c')