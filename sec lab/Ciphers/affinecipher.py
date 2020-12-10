def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None 
  else: 
    return x % m 
 
def encrypt(text, key): 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


def decrypt(cipher, key): 
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 
key = list(map(int,input("Enter the Key: ").split()))
while True : 
     
    t = 0
    opt = int(input("\nEnter option \n1. Enter text \n2. Encrypt & Decrypt\nEnter Option: "))
    if opt == 1 : 
        text = input("\nEnter plain text: ")
    if opt == 2 : 
        if text == "": print("No Plain Text")
        else:
          enc_text = encrypt(text, key) 
          print('Encrypted Text: {}'.format(enc_text)) 
          print('Decrypted Text: {}'.format(decrypt(enc_text, key) )) 
        
# Enter the Key: 233 377

# Enter option
# 1. Enter text
# 2. Encrypt & Decrypt
# Enter Option: 1

# Enter plain text: sabrish

# Enter option
# 1. Enter text
# 2. Encrypt & Decrypt
# Enter Option: 2
# Encrypted Text: VNMWFVG
# Decrypted Text: SABRISH        


