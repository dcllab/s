def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
ip = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", ip)
print("after encryption: ", encrypt(ip, s))

# enter string: sabrishh 
# enter shift number: 3
# original string:  sabrishh
# after encryption:  vdeulvkk