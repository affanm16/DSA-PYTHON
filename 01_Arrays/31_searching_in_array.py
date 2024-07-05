# using linear search here
import array
my_arr=array.array('i',[10,20,30,40,50,33,23,99])
def linear_search(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i
    return -1

print(linear_search(my_arr,103))
print(linear_search(my_arr,23))