#linear Search

import numpy as np
twoDArray=np.array( [ [21 ,35 ,40 ,37],[20, 38, 43, 29],[21, 30 ,39 ,38],[20 ,31, 50, 44] ] )
print(twoDArray)

def search_linear(array,value):
    for i in range(len(array)):  #gives number of rows ->o(m)
        for j in range(len(array[0])): #gives number of columns->O(n)
            if array[i][j]==value:
                return 'the element is located at index ' +str(i)+" "+str(j)
    return 'the element is not found'

search=search_linear(twoDArray,29)
print(search)

#time and space complexity is O(mxn),O(1) respectively