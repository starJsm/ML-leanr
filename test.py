from math import log

a = 8/13.0
b = 5/13.0
c = 13/17.0
d = 5/17.0
e = 8/9.0
sum = -(a*log(a, 2) + b*(log(b, 2)))
# sum1 = -(c*log(c, 2) + d*(log(d, 2)))
print(0.998 - c*sum)