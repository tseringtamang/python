student={'name':'ram', 
         'age':20,
         'address':'boudha'
         }

print(student)

#task 
capital ={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys()) #gives list of keys in the dictionary
print(capital.values()) #gives list of values in the dictionary

print(capital["Nepal"]) # gives the value of given key
capital['Japan'] = "Tokyo" #adds the value in the dictionary
print(capital)
capital['Bhutan'] = "Thimpu" 
print(capital)

pop_element = capital.pop ("Bhutan")
print(pop_element)
print(capital)

marks = {
    "Maths" :80,
    "Science":80,
    "Nepali":80
}
print(marks)
capital.update(marks)
print(capital)

a ={1,2,3,4}
b =(1,2,3,4)

#list remaining part
c =['a','b','c','e','d','f']
print(c.index('a')) #gives the index number of given data 
c.sort() #ascending order
print(c)
c.sort(reverse=True) #decending order
print(c)

copy_capital = capital.copy()
print(copy_capital)
clearcapital =capital.clear()
print(clearcapital)