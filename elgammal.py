
import random 
from math import pow

a = random.randint(2, 10) 

def gcd(a, b): 
  if a < b: 
    return gcd(b, a) 
  elif a % b == 0: 
    return b; 
  else: 
    return gcd(b, a % b) 

# Generating large random numbers 
def gen_key(prime): 

  key = random.randint(pow(10, 20), prime) 
  while gcd(prime, key) != 1: 
    key = random.randint(pow(10, 20), prime) 

  return key 

# Modular exponentiation 
def power(base, exp, MOD): 
  x = 1
  y = base 
  while exp > 0: 
    if exp % 2 == 0: 
      x = (x * y) % MOD; 
    y = (y * y) % MOD 
    exp = int(exp / 2) 
  return x % c 

# Asymmetric encryption 
def encrypt(msg, prime, receiverPublicKey, generator): 

  en_msg = [] 

  senderKey = gen_key(prime)# Private key for sender 
  sharedKey = power(receiverPublicKey, senderKey, prime) 
  senderPublicKey = power(generator, senderKey, prime) 
  
  for i in range(0, len(msg)): 
    en_msg.append(msg[i]) 

  print("g^k used : ", p) 
  print("g^ak used : ", sharedKey) 
  for i in range(0, len(en_msg)): 
    en_msg[i] = sharedKey * ord(en_msg[i]) 

  return en_msg, senderPublicKey 

def decrypt(en_msg, senderPublicKey, receiverPrivatekey, prime): 

  dr_msg = [] 
  h = power(senderPublicKey, receiverPrivatekey, prime) 
  for i in range(0, len(en_msg)): 
    dr_msg.append(chr(int(en_msg[i]/h))) 
    
  return dr_msg 

# Driver code 
def main(): 

  # msg = 'encryption'
  msg = input();
  print("The given message ", msg) 

  prime = random.randint(pow(10, 20), pow(10, 50)) 
  generator = random.randint(2, prime) 

  receiverPrivateKey = gen_key(prime)# Private key for receiver 
  receiverPublicKey = power(generator, receiverPrivateKey, prime) 
  print("g used : ", generator) 
  print("g^a used : ", receiverPublicKey) 

  en_msg, senderPublicKey = encrypt(msg, prime, receiverPublicKey, generator) 
  dr_msg = decrypt(en_msg, senderPublicKey, receiverPrivateKey, prime) 
  dmsg = ''.join(dr_msg) 
  print("Decrypted Message :", dmsg); 


if __name__ == '__main__': 
  main() 