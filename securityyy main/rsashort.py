from math import gcd 
p = int(input())
q = int(input())
plain = int(input())
n = p*q 
phi = (p-1) * (q-1) 
for e in range(2,phi): 
    if gcd(e,phi) == 0 : break 
for i in range(1,phi): 
    x = i*phi + 1 
    if x%e == 0:
        d = int(x/e)
        break 
cipher = pow(plain,e)%n 
decipher = pow(plain,d) %n