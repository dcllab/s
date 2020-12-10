from math import gcd
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
plain = int(input('Enter the value = '))
n = p*q
phi = (p-1)*(q-1)
for e in range(2,phi):
    if gcd(e,phi)== 1: 
        break
for i in range(1, phi): 
    x = 1 + i * phi
    if x % e == 0: 
        d = int(x/e) 
        break
cipher = pow(plain,e) % n
decipher = pow(cipher,d) % n 
print('n = '+str(n)+' e = '+str(e)+' t = '+str(phi)+' d = '+str(d))
print(' cipher text = '+str(cipher)+' decrypted text = '+str(decipher))