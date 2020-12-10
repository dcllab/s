user_list = []
file_list = []

def addUser():
  addEntity(user_list)

def addFile():
  addEntity(file_list)

def addEntity(l):
  print('Enter name: ')
  name = input()
  print('''Enter access level:
  1. Normal
  2. High
  3. Higher
  ''')
  type = int(input())
  l.append((name, type))

def printBellTable():
  for user in user_list:
    print()
    print(user[0], end=' ')
    for file in file_list:
      if user[1] == file[1]:
        print(file[0] + ' - R/W', end=' ')
      elif user[1] > file[1]:
        print(file[0] + ' - Read', end=' ')
      else:
        print(file[0] + ' - Write', end=' ')

def printBibaTable():
  for user in user_list:
    print()
    print(user[0], end=' ')
    for file in file_list:
      if user[1] == file[1]:
        print(file[0] + ' - R/W', end=' ')
      elif user[1] > file[1]:
        print(file[0] + ' - Write', end=' ')
      else:
        print(file[0] + ' - NA', end=' ')


while True:
  print('''
  1. To add a new person
  2. To add a new file
  3. See the Bell laPadula access table
  4. See the BIBA access table
  Anything else to quit ''')

  o = int(input())

  if o == 1:
    addUser()
  elif o == 2:
    addFile()
  elif o == 3:
    printBellTable()
  elif o ==4:
    printBibaTable()
  else:
    break