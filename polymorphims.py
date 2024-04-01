# class Vehicle:
#     def __init__(self,name, color, price):
#         self.name = name 
#         self.color = color
#         self.price = price

        
#     def show (self):
#         print('details:',self.name,self.color,self.price)
    
#     def max_speed(self):
#         print('Vehicle max speed is 150')

#     def change_gear(self):
#         print('Vehicle change is 6 gear')

# class Car(Vehicle):
#     def max_speed(self):
#         print('car max speed is 240')

#     def change_gear(slef):
#         print('Car change 6 gear')

# car = Car ('car x1','red',20000)
# car.show()
# car.max_speed()
# car.change_gear() 

# #calculating the area of different shapes. We'll create a base class shape with an area()method , and then create subclasses 
# #for sepcific shape shapes like rectangle, circle and triangle which will override()method to calculate the area specific to each shape

# import math
# class Shape:
#     def area(self):
#         raise NotImplementedError("subclasses must implement this method ")
    
# class Rectangle(Shape):
#   def __init__(self, width, height):
#       self.width =width
#       self.height =height

#   def area(self):
#       return self.width*self.height
  
# class Circle(Shape):
#    def __init__(self,radius):
#        self.radius =radius

#    def area(self):
#        return math.pi*self*radius** 2

# class Triangle(Shape):
#     def __init__(self,base,hieght):
#         self.height = height
#     def area(self):
#         return 0.5* self.base*self.height
    
# Rectangle = Rectangle(5,4)
# circle = Circle(3)
# triangle= Triangle(6,8)

# print("area of rectangle:",Rectangle.area())
# print("area of circle:", circle.area())
# print("area of triangle:",triangle.area())
      
      
class Employee:
    def __init__(self,name,project,salary):
        self.name = name #public member (accessible within or outside of a class)
        self._project = project #protected member(accessible with the class and it's sub-class)
        self.__salary = salary # private member (accessible only within a calss)

    def show(self):
        print("Name :",self.name)

emp = Employee ('Madhav','Xavier',1000)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)