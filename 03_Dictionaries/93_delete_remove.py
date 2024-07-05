myDict={'name': 'affan', 'age': 21, 'address': 'hyd'}
del myDict['address']
print(myDict)


# to pop last item use popitem()
popped=myDict.pop('age')
print(popped)

#CLEAR()
myDict.clear()
print(myDict)