# function is a block of code.we used fucntion to reuse the code.two type of function
#Build-in function
#user defined fucntion

#def function_name():
    #function boby

    #function_name()

#def helloworld():
#    print("helloworld")

#helloworld()
 #position argument - takes value according to proper positional order.
# def hello(name,course_name): #parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)
# hello('ram','python with django')#arguments

# #key word arguments -takes value accodrding to keywrd
# def hello(name,course_name):
#     print("hello",name,"welcome to wed development training ")
#     print(course_name)
# hello('python with django','ram')
# hello(name='ram',course_name='python with django')

# #defalut argument
# def hello(name,course_name):
#     print("hello",name,"welcome to wed development training ")
#     print(course_name)
# hello(name='ram',course_name='python with data science')


# def sum(a,b):
#     total= a+b 
#     return total # returns gives result of function 
 
# result = sum (2,3)
# print(result)

# #args -> 
# def sum (*args):
#     total = 0
#     for n in args:
#         total += n
#         return total 
#     result = sum(2,3,4)
#     print(result)
# #abritrary keyword argument -
# def hello (**kwargs ):
#     print("hello", kwargs['name'],"welcome to web development training")
#     print(kwargs['course_name'])

# hello(name = 'ram',course_name ='python with data science', another_course = 'python with data science')
# #scope of variable 
# #global variable -> which can accessible from outside the function. its 
l = float(input('enter length:'))
w = float(input('enter wide:'))
 

def area():
#     #local variable -> that is defined inside the function and cannot accessible from outside the function . Its scope is only around the delared function

   h = float(input('enter a h :'))
   area_of_object = 1*w
   return area_of_object

# def volume():
#     h = float(input('enter a height :'))
#     v = 1 *w* h 
#     return v 
# result = area ()
# result_volume = volume ()
# print (result)
# print(result_volume)

#lambda function : the fucntion without name. It is used for instant use and its one-time uses.
#lembda keyword is used. 

# x = lambda a,b:a + b
# sum = x (2,3)
# print(sum)

# x = lambda a , b : a*b
# area = x (2,3)
# print(area) 

#recursive function-function calling itself again and again
# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n*factorial(n-1)
    
# a = factorial(4)
# print(a)

    