#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref6.py,v 1.1 2012-01-10 08:45:33 luis Exp $

def fun1(l):
    l = l + [4,5]
def fun2(l):
    l.extend([4,5])
def fun3(l):
    return l.extend([4,5])
    
x=[0,1,2]
fun1(x)
print "c1-x:", x
#print "c1-z:", z
fun2(x)
print "c2-x:", x
x = fun3(x)
print "c3-x:", x[0]



