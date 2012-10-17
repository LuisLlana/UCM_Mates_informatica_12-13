#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref8.py,v 1.1 2012-01-10 08:45:33 luis Exp $


def fun(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

x=12
y=18
z=fun(x,y)
print "c1-x:", x
print "c1-y:", y
print "c1-z:", z

x=3000
y=7
z=fun(x,y)
print "c2-x:", x
print "c2-y:", y
print "c2-z:", z
