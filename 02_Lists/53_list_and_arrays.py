#similarities
# 1->both are mutable i.e can be updated
# 2->both can be indexed and iterated through
#3->they both can be sliced


#differences
# arrays are gnerally used for arithmetic operations
import numpy as np
myarray=np.array([1,2,3,4,5,6,7])
myList=[1,2,3,4,5]

print(myarray/2)
print(myList/2)

#in arrays the values should be of same types
#in list the data types can be any