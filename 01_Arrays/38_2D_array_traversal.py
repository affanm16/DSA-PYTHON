import numpy as np
twoDArray=np.array( [ [21 ,35 ,40 ,37],[20, 38, 43, 29],[21, 30 ,39 ,38],[20 ,31, 50, 44] ] )
print(twoDArray)

def traversal_2d(array):
    for i in range(len(array)):  #gives number of rows ->o(m)
        for j in range(len(array[0])): #gives number of columns->O(n)
            print(array[i][j])

traversal_2d(twoDArray)

#time complexity ->O(mxn),space-O(1)
