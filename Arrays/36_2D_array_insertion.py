# we can add a column/row but not a single value

# Adding column
import numpy as np
twoDArray=np.array( [ [21 ,35 ,40 ,37],[20, 38, 43, 29],[21, 30 ,39 ,38],[20 ,31, 50, 44] ] )
print(twoDArray)
twoDArray=np.insert(twoDArray,3,[[1,2,3,4]],axis=1) #3 is the position
print(twoDArray)

# adding row
twoDArray=np.insert(twoDArray,4,[[-1,-2,-3,-4,-5]],axis=0) #3 is the position,0 is row
print(twoDArray)

#by using append() we can also append a row or column