# write a program to find all pairs of integers whose sum is equal to given number
#conditions => the pairs should be distinct i.e (3,3) is invalid


def findPairs(arr,value):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                continue
            elif arr[i]+arr[j]==value:
                print(i,j)

mylist=[1,2,4,3,3,6,0]
target=6
findPairs(mylist,target)