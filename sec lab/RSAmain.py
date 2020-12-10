#RSA Algo
import math
p = int(input("prime number for p: "))
q = int(input("prime number for q: "))

def prime_check(a): # to check if prime or not
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True

check_p = prime_check(p)
check_q = prime_check(q)

while(((check_p==False)or(check_q==False))):
    p = int(input("prime number for p: "))
    q = int(input("prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

n = p * q #rsa modulous calculation
print("RSA Modulous 'n' = ",n)

r= (p-1)*(q-1) #Eulers toitent
print("Eulers toitent 'r' = ",r)

# Calculation of e
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    # print("Value of e by gcd = ", e)
    return e

#calculating the Euclids algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                pass
            r=e
            e=b
def eea(a,b): 
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)

# to calcuate multiplicative inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            pass
        elif(s>0):
            print("multiplicative inverse 's' =", int(s))
        return s%r
# to find e - for e,r to be coprime       
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print(" value of e = ",e)
eugcd(e,r)
d = mult_inv(e,r)
# print("d =  ",d)
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public) 
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n # formulae
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x    
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n #fromulae
            m+=65
            c=chr(m)
            x+=c
    return x
message = input("Enter text for encryption OR enter array value for decryption:")
print("msg : ",message)
opt = input("Enter Option:\n1.Encrypt\n2.Decrypt\nOption: ")
if(opt=='1'):
    enc_msg=encrypt(public,message)
    print("encrypted message :",enc_msg)
elif(opt=='2'):
    print("decrypted message :",decrypt(private,message))
else:
    exit