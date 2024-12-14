import random

# file_name = 'f1.txt'
# file = open(file_name, mode='w')
# #
# try:
#    for i in range(1000):
#   #     file.write('text \n')


#finally:
 #   file.close()

#file_name = 'f2.txt'
#with open(file_name, 'w') as file:
 #   for i in range(0, 100):
  #      file.write(str(random.randint(1, 10000)) + '\n')


#with open('f1.txt', 'r') as file:
#     content = file.read()
#     print(content)

with open('f1.txt', 'r') as file:
    line = file.readline()
    print(line)
    while line:
        print(line)
        #наш кодик
        line = file.readline()