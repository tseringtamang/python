#exception ->an event that occurs the normal to disrupt the normal flow of operation
# try:
#     age = int(input())
#     print(age)

# except:
#     print('please provide numberic value')
#      print('xavier college')

# try:
#     a=int(input('enter the value'))
#     b=int(input('enter the value'))
#     c=a/b
# except ValueError:
#     print('please provide numeric value')
# except ZeroDivisionError:
#     print("Zero will not divide any other number")
# else:
#     print("the value of c is",c) 

user1 = 'admin'
pass1 = 'admin'
def login():
  user1 = 'admin'
  pass1 = 'admin'
try:
    username =input("enter a username=")
    password =input("enter a username= ")
    
    if user1 != username:
        raise ZeroDivisionError
    elif pass1 != password:
        raise ValueError
except ZeroDivisionError:
    print("username is invalid")
    login()
except ValueError:
    print("password is invalid")
    login()
else:
    print("login successful ")
finally:
    print("home")
login