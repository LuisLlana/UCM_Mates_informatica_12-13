#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref5.py,v 1.1 2012-01-10 08:45:33 luis Exp $

x = [0,1,2,3]
y = [x,x+[4],x]
x.append(5)
print "c1-y:", y
print "c1-x:", x

x = [6,7,8,10]
y[0] = 1
print "c2-y:", y
print "c2-x:", x

z=x[2:4]
z[0]=-1
print "c3-z:", z
print "c3-x:", x
