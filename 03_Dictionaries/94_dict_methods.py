#clear()
myDict={'name': 'affan', 'age': 21, 'address': 'hyd'}
myDict.clear()
print(myDict)

#copy() doesn't modifies original one 
myDict1={'name': 'affan', 'age': 21, 'address': 'hyd'}
dict=myDict1.copy()
print(dict)

#fromkeys->[keys,values]
new_dict={}.fromkeys([1,2,3,4],0)
print(new_dict)

#get->returns the value for specified key 
#dictionary.get(key,value),where value parameter is optional which is 
# printed incase the key is not found

myDict2={'name': 'affan', 'age': 21, 'address': 'hyd'}

print(myDict2.get('age',27))
print(myDict2.get('city',90))

#items() ->returns list of tuples pair
print(myDict2.items())

#keys->it diplayes the keys
print(myDict2.keys())

#popitem()
print(myDict2.popitem())

#setdefault()->returns the value of key is in the dict,if key is not present it inserts
myDict3={'name': 'affan', 'age': 21, 'address': 'hyd'}
print(myDict3.setdefault('pin','123'))
print(myDict3)

#pop()->pops the specified key value
#values->returns list having all values
print(myDict3.values())

#update method->updates the key value

dict2={'a':1,'b':2}
myDict3.update(dict2)
print(myDict3)