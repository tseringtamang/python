
# list 
thislist=["python","java","C++"]
print(thislist)

#list task 
laptops = ['dell','hp','sony','lenovo','mac']

laptops.append('microsoft')
print(laptops)
laptops.insert(-1,'microsoft')
print(laptops)
laptops.remove("dell")
print(laptops)
removed_element = laptops.pop(3)
print(removed_element)
print(laptops)

a=[1,2,3,4,5]

laptops.extend(a)
print(laptops)
b=[6,7,8,9,10]
laptops.extend(b)
print(laptops)

laptops=['dell','hp','mac','sony']
laptops.append('microsoft')
print(laptops)
count=a.count(1)
print(count)
copy_list = laptops.copy()
print("this is an orginal list:",laptops)
print("this is a copy list:",copy_list)
copy_list.clear()
print(copy_list)

#tuple  
number=(1,2,3,2,2)
print(number)
count=number.count(2)
print(count)

#set 
user_id= {111,112,113,114}
print(user_id)

a = {1,2,3,4,5}
a.add(6)
a.add('Nepal')
print(a)
a.remove(5)
print(a)
b=a.copy()
print(b)
b.clear()
print(b)

#difference
A ={'a','b','c','d','e'}
B ={'f','b','c','d','g'}
print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))

re=a.pop()
print(re)
y = {'a','b','c','d'}
rel = y.remove('a')
print(rel)
print(A.symmetric_difference(B))
print(A.union(B))

