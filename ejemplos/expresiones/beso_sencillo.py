#beso exacto
# -*- coding: utf-8 -*-
from math import sqrt  

radio1 = 1.1
radio2 = 2.3
radio3 = 4.0

# transformo los radios
s1 = 1/float(radio1)
s2 = 1/float(radio2)
s3 = 1/float(radio3)
# despejamos la ecuación
a = s1**2 + s2**2 + s3**2
b = s1 + s2 + s3
# Nos queda la ecuación 2(a + s4^2) = (b + s4)^2
sol1 = b + sqrt(2*(b**2 - a))
sol2 = abs(b - sqrt(2*(b**2 - a)))
# radio del circulo pequeño
radio4_1 = 1 / sol1
# radio del circulo mayor
radio4_2 = 1 / sol2
print radio4_1, radio4_2


