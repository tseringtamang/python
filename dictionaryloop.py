dictionary = {}

dictionary['name'] = "Ram"
dictionary['age']=18
dictionary['subject']=['math','science','nepapli']
dictionary['education']={
    'school':{
    'name' :'Xavier School',
    'address':'Kalopul,Kathmandu'
      },
'high school' : {
    'name':'DAV College',
    'address': 'jawlakha,latipur'
            },
'Bachelor level' :{
    'name':'xavier college',
    'address':'boudha,kathmandu'
    }          

}
print(dictionary)


#for i in dictionary.keys():
#print(i)


#for i in dictionary ['subject'][0]:
 #   print(i)
     
#for i in dictionary[ 'education'] :
#    print(i)
 
#for i ,j in dictionary['education']['school'].items():
  #  print(i,j)

#dictionary = {key ;}

print(dictionary['education']['school']['name'])
print(dictionary['education']['high school']['name'])