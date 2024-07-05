tuple1=('a','b','c','d','e')
tuple2=('f','g','h','i','e')
print(tuple1+tuple2)

print(tuple1*3)

#methods
#count()->no of elements
print(tuple2.count('f'))

#index method
print(tuple2.index('i'))

#len() 
#max()
print(max(tuple1))
print(min(tuple2))

#tuple method-> converts a list to tuple
print(tuple([1,2,3]))