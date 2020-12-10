import hashlib 

ip = input("enter a string : ")

e1 = hashlib.sha1(ip.encode())
print(e1.hexdigest())

e2 = hashlib.sha256(ip.encode())
print(e2.hexdigest())

e3 = hashlib.sha512(ip.encode())
print(e3.hexdigest()) 

