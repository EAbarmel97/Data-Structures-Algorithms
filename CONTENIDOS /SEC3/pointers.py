num1  = 11 #apunta a un cierto espacio en memoria
num2 = num1  #apunta a un cierto espacio en memoria 

print(id(num1))
print(id(num2))

num2 = 22


print(id(num1))
print(id(num2))

## compobamos si apuntan al mismo espacio en memoria usando dicts 

dict1  ={ "val": 11} 
dict2 = dict1

print(id(dict1))
print(id(dict2))

dict2["val"] = 22

print(id(dict1))
print(id(dict2))