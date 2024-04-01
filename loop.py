color = ['red','blue','black','white']
fruits = ['apple','mango','papaya','orange']
#i = fruits[0]
#print(i)
# i = friuts[1]
#print(i)

#for loop - iteration over sequence
for i in fruits:
    print(i)

for i in range(5):
    print(i)


for x in range(1,20,2):
    print(x)


#task 
for i in range(11):
    print(i)
    if x % 2 == 0 :
       print ("given number is even") 
    else:
        print ( "given number is odd")

for i in range(1,11):
    #print(i)
    #if i== 5 :
    #   break
    #print(i)
    #if i == 5 :
    #  continue
    #print(i)
    pass
    print(i)

    #while loop -repeat the code if certain condition is meet or true

    y = 0
    while y<=10:
        #print(y)
        y +=1

        #if y == 5:
        #    break
        #print(y)

        #if y == 5 :
         #   continue
        #print(y)

        for x in color:
            for y in fruits:
                print(x,y)



