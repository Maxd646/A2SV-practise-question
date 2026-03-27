from math import comb
s1= input().strip()
s2= input().strip()
n= s2.count("?")
a= s1.count("+")-s2.count("+")
if n<a or a<0:
    print(0)
else:
    print(comb(n, a)/(2**n))