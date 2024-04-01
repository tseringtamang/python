import os, shutil
#file handling ->open file, close file , read file write and maintain file
path = r'C:\Users\Acer\Desktop\hello/test.txt'
# my_files= open (path)
# print(my_files)
# print(my_files.read())
# print(my_files.writable()) #to check whether to write in files or not
# my_files.close()

# my_another_files = open(path, 'r+')
# print(my_another_files.readable())
# print(my_another_files.writable())
# print(my_another_files.read())
# my_another_files.write('ram  \n')


# my_another_files = open(path, 'w+')
# print(my_another_files.readable())
# print(my_another_files.writable())
# # print(my_another_files.read())

# my_another_files.write('ram')
# print(my_another_files.seek(1))
# print(my_another_files.read())


my_next_file =open('next.txt','a+')
print(my_next_file.readable())
print(my_next_file.writable())
my_next_file.write('hello world')
print(my_next_file.write('hello \n world'))

print(my_next_file.seek(0))
print(my_next_file.read())
print(my_next_file.readline())
print(my_next_file.readlines())

list1=['\n ram \n','\nshyam\n','\nhari\n']
print(my_next_file.writelines(list1))

shutil.copy('next.txt','next1.txt')

shutil.move('test.txt','next1.txt')