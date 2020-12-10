#secure hash algorithm 

import hashlib
str = input("Enter a String: ")
result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ", result.hexdigest(), "\n")

result = hashlib.sha224(str.encode())
print("The hexadecimal equivalent of SHA224 is : ", result.hexdigest(), "\n")

result = hashlib.sha256(str.encode())
print("The hexadecimal equivalent of SHA256 is ", result.hexdigest(), "\n")

result = hashlib.sha384(str.encode())
print("The hexadecimal equivalent of SHA384 is ", result.hexdigest(), "\n")

result = hashlib.sha512(str.encode())
print("The hexadecimal equivalent of SHA512is :", result.hexdigest(), "\n")



