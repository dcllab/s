user_list = [] 
file_list = [] 

def addUser(): 
    addEntity(user_list) 

def addFile():
    addEntity(file_list)

def addEntity(l):
    name = input("enter name : ") 

    print("Enter access level: \n1. Unclassified\n2. Confidential\n3.Secret\n4. Top secret")
    type = int(input("enter the type : ")) 
    l.append((name,type))

def printTable():
    for user in user_list:
        print("\n",user[0],end='')
        for file in file_list: 
            if user[1] == file[1] : user_list = []
file_list = []

def addUser():
  addEntity(user_list)

def addFile():
  addEntity(file_list)

def addEntity(l):
  print('Enter name: ')
  name = input()
  print('''Enter access level:
  1. Unclassified
  2. Confidential
  3. Secret
  4. Top Secret
  ''')
  type = int(input())
  l.append((name, type))

def printTable():
  for user in user_list:
    print()
    print(user[0], end=' ')
    for file in file_list:
      if user[1] == file[1]:
        print(file[0] + ' - RW', end=' ')
      elif user[1] > file[1]:
        print(file[0] + ' - R', end=' ')
      else:
        print(file[0] + ' - W', end=' ')

while True:
  print('''
  1. To add a new person
  2. To add a new file
  3. See the access table
  Anything else to quit ''')

  o = int(input())

  if o == 1:
    addUser()
  elif o == 2:
    addFile()
  elif o == 3:
    printTable()
  else:
    break
                print(file[0]+ ' - RW', end= ' ')
            elif user[1] > file[1] : 
                print(file[0]+ ' - R', end = ' ')
            else : 
                print(file[0] + ' - W', end = ' ')

while True : 
    print('''
    1. To add a new person
    2. To add a new file
    3. See the access table
    Anything else to quit ''')

    option  = int(input(" enter the option : "))
    if option == 1 : 
        addUser()
    if option == 2 : 
        addEntity()
    if option == 3 : 
        printTable()
    else: break 
