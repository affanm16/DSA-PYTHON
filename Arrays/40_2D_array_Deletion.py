# deletion doesn't happen permanently instead a new array is created
#time and space complexity will be O(mxn) ->as the rows and cols are copied and takes new space



import numpy as np
twoDArray=np.array( [ [21 ,35 ,40 ,37],[20, 38, 43, 29],[21, 30 ,39 ,38],[20 ,31, 50, 44] ] )
print(twoDArray)
newArray=np.delete(twoDArray,2,axis=0)
print(newArray)