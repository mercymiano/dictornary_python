
student = {
    "fname": "james",
    "lname": "Bond",
    "phone": 2657785667,
    "Email": "jamesbond@gmail.com"
}
print(student)

car = {
    "brand": "Ford",
    "electric": False,
    "year": 2025,
    "colors": ["red","white","blue"]
}
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
#accessing the items
x= car["model"]
print(x)
#using get
x= car.get("model")
print(x)
#get keys
x= car.keys()
print(x)
#get values
x= car.values()
print(x)


#checking if key exist
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
if "model" in car:
    print("yes, 'model' is one of the keys in this dict dictionary")

 #change dictionary items
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
car["year"]= 2018
print (car)
#add dictionary items
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
car["color"] ="red"
print(car)

car["color"] ="red","blue","green"
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
#removing using pop()
car.pop("model")
print(car)
#using popitem()
car.popitem()
print(car)
del car["model"]
print(car)
#using clear()
car.clear()
print(car)

#loop trough a dictonary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
for x in car:
    print(x)
for x in car.values():
    print(x)
for x in car.keys():
    print(x)  

#nested dictionaries
child1= {
    "name":"emily",
    "year": 2004
}
child2= {
    "name":"Tobia",
    "year":2007
}
child3= {
    "name":"Jane",
    "year":2067
}
myfamily= {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
