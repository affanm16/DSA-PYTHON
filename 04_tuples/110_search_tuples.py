tuple1=('a','b','c','d','e')

#method in method
print('e' in tuple1)
print('m' in tuple1)

#index method
print('e' in tuple1)
print(tuple1.index('c'))
# print(tuple1.index('l'))

# method
def searchtuple(tuple1,element):
    for i in range(0,len(tuple1)):
        if tuple1[i]==element:
            return f"the element is found ar {i} index"
    return 'The element is not found'
print(searchtuple(tuple1,'e'))