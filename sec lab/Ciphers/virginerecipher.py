def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    return ciphertext
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)

    return plaintext

ip = input("PT:")
key = input("Key : ")
while(True):
    opt = int(input("\n0.Re-enter the plaintext and key\n1.Encrypt\n2.Decrypt\nenter option: "))
    if opt == 0:       
        ip = input("Text:")
        key = input("Key : ")
    elif opt == 1:
        print(encrypt(ip,key))
    elif opt == 2:
        print(decrypt(ip,key))


# print(encrypt(ip,key))
# print(decrypt(ip,key))

# Text:sabrishh
# Key : vidpra
# ZUQSLEOB
# sabrishh