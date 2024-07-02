#create an array


#method-1 ->using 'array' module
import array
my_arr=array.array('i') #i->integer
print(my_arr)
#empty array creation results in constant time complexity O(1)
#space complexity will also be O(1)

my_arr=array.array('i',[10,20,30,40]) #i->integer
print(my_arr)
#time complexity-O(n),space complexity-O(n)



#method-2 ->using  'numpy' module
import numpy as np
my_arr1=np.array([],dtype=int)
print(my_arr1)
#empty array creation results in constant time complexity O(1)
# ""  space complexity will also be O(1)


my_arr2=np.array([10,20,30,40])
print(my_arr2)
#time complexity-O(n),space complexity-O(n)