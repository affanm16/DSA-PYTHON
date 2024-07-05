#in operator works on keys only

myDict={'name': 'affan', 'age': 21, 'address': 'hyd'}
print('name' in myDict)

# for values use values()
print('affan' in myDict.values())

#LEN()
print(len(myDict))

#all() ->True-all keys are true/false
print(all(myDict))

#sorted()->keys will be sorted
print(sorted(myDict))