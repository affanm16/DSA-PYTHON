#to check whether a list is permutation of another or not

def permutation(l1,l2):
    if len(l1)!=len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

list1=[1,2,3,4,5]
list2=[5,4,1,2,3]
print(permutation(list1,list2))