a = "hello, world!"
print(a[1])

#length 
a = "hello, world!"
print(len(a))

b = "hello, world!"
print(b[7:12])

#modify string 
a = "Hello,World!"
print(a.lower())

a = "hello,world" 
print(a.replace("world","Nepal"))

a = "hello, world!"
print(a.split(" "))

#string Contcatention 
a = "hello"
b = "world"
c = a+b 
print(c)
#format string 
quantity = 3 
itemno= 567
price=49.95
myorder="i want {} pieces of item {}for{}dolloars."
print(myorder.format(quantity,itemno,price))

#task 
a = "My Country Name is Nepal"

print(len(a))
print(a[19:24])
print (a.lower())
print(a.replace("Nepal","America"))
print(a.split(" "))
#task 2

b = "I Am Studying At Xavir College"

print(len(b))
print(b[-1])
print(b.lower())
print(b.replace("Xavir","Harvard"))
print(b.split(" "))

# format task 
quantity=5
itemno=957
price=43.35
myorder="i want {} pieces of item {} for {} dolloars."
print(myorder.format(quantity,itemno,price))


