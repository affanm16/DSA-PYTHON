#How to check if any array contains a particular number in python
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])

def findNumber(array,value):
    for i in range(len(array)):
        if array[i]==value:
            print(i)

findNumber(arr,6)
