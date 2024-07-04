#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]
target=10

def linear_search(p_list,target):
    for i,value in enumerate(p_list):
        if value==target:
            return i
    return -1


print(linear_search(myList,target))