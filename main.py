# myFile = open('MyCarShop.txt', 'w')
# myFile.close()

# myList = ['\nUral', '\nVespa', '\nBMW X6']
# with open('MyCarShop.txt', 'a') as file:
#     file.writelines(myList)
# print('File writed')

# with open('academy.txt', "a") as myfile:
#    print('Academy TOP', file=myfile)

# with open('MyCarShop.txt', "r") as file:
#   for line in file:
#      print(line, end="")

# with open('MyCarShop.txt', "r") as file:
#   str1 = file.readline()
#   print(str1, end='')
#   str2 = file.readline()
#   print(str2, end="")

# with open('MyCarShop.txt', "r") as file:
#   line = file.readline()
#   while True:
#       print(line, end="")
#       line = file.readline()

# with open('MyCarShop.txt', "r") as file:
#   content = file.readlines()
#   str1 = content[0]
#   str2 = content[1]
#   str3 = content[2]
#   print(str3)
#   print(str2)

#   filename = "academy.txt"
#   with open(filename, encoding='UTF-8') as file:
#       text = file.read
#       print()

#with open("hello.txt", "w+") as file:
#    file.write('Hello, World')
#   file.seek(0)
#     content = file.read()
# print(content)

filename = "messages.txt"

def write():
    messages = input("Type message ")
    with open(filename, "a") as file:
        file.write(messages + "\n")

def read():
    with open(filename, "r") as file:
        for messages in file:
            print(messages, end="")
    print()

while (True):
    selection = int(input('1. Write to file\n 2. Read file\n 3. Exit\n'))
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print('Wrong enter')
print('See you! :D')