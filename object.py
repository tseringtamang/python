#OOP in python (object oriented program). we deal with real time obejct and its entities

# class Room:# blueprint of object.
#     l = int(input("enter a length :"))
#     w = int(input("enter a width :"))
#     def area(self):
#         print("area of room is ",self.l*self.w)
        
# area_of_room = Room()
# print(area_of_room.area())


# class Room:
#     l = int (input("enter a length :"))
#     h = int(input("enter a height :"))
#     w = int(input("enter a width:"))
#     def volume(self):
#         print("volume of room",self.l*self.h*self.w )

# volume_of_room = Room()
# print(volume_of_room.volume())




class  calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sub(self,*arges):
        self.num1 = arges[0]
        total = 0
        for n in arges:
            total -= n 
        return total
    def add(self,*arges,**kwargs):
        for n in arges:
            total += n 
            return total
    def multiply(self,num1,num2):
        return  num1 * num2
    
    def divide (self, num1, num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("error: Division by zero!")
cal = calculator(1,2)
print(cal.num1)
print(cal.sub(2,3,))
