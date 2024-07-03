import array
my_arr=array.array('u',["A","B","C","D"]) #u->unicode

def accessElements(arr,index):
    if index < len(arr):   #-->O(1)
        print(arr[index]) #-->O(1)
    else: #-->O(1)
        print("please insert valid index")

accessElements(my_arr,3)

#space complexity is also-->O(1)