import numpy as np
twoDArray=np.array( [ [21 ,35 ,40 ,37],[20, 38, 43, 29],[21, 30 ,39 ,38],[20 ,31, 50, 44] ] )
print(twoDArray)
def accessElements(arr,rindex,cindex):
    if rindex>=len(arr) or cindex>=len(arr[0]):
        print("incorrect index")
    else:
        print(arr[rindex][cindex])
accessElements(twoDArray,3,3)
# time and space comp-O(1)