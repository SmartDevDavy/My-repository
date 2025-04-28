#dictionaries store items in key:value pairs and they are changable, ordered and don't allow duplicates
person = {
'name':'James',
'color':'brown',
'age':23
}
print(person)
print('name of the person is', person['name'])#you can access the value using the key 
print('my dictionary has', len(person), 'entities')
#a dictionary can contain any data type
mycity = {
'name':'Nakuru',
'isClean':True,
'concistuencies':['Bahati','Nakuru East','Nakuru West']
}
print(mycity)
name = mycity['name']#accessing item using key
print(name)
name = mycity.get('name')#accessing using .get()
print (name)
y = person.keys()#geting keys of a dictionary
print(y)
x = person.values()#geting values of a dictionary
print(x)
z = person.items()#returns items as a tuple
print(z)

#adding new item or changing an item
person['religion'] = 'Christian' #method 1
print(person)
#dictionary['key'] = 'value'
person.update({'religion':'muslim'})#rem '{}' inside
print(person)


#cheking if a key exists
if 'religion' in person:#don't forget the colon'
    print('Religion key is available in your dictionary')
 
 #removing an item
person1 = {
  'height':6.7,
  'color':'black',
  'nationality':'Kenyan'
 }
print(person1)
person1.pop('color')
print(person1)
person.popitem()
print(person,'religion has been removed bcz its the last one')#removes the last item
del person['color']#removes both the key and value
print(person)
#del person - it will delete the dictionary completely
#person1.clear() - empties the dictionary

#looping a dicionary
business= {
'street':'Kijabe',
'laneNo':'lane 2',
'house':'dsm place'
}
print (business)
for x,y in business.items():#loops both key & value
    print(x,y)
    
for x in business:#loops only through keys
    print(x)

for x in business.values():#loops only through values
    print(x)

#copying a dictionary
buzz = business.copy()#method1
print(buzz)
buzz = dict(business)#method2
print(buzz)

#nesting dictionaries
#method1
general = {
'value1':person,
'value2':business
}
print(general)
#method2
myfamily = { 
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
