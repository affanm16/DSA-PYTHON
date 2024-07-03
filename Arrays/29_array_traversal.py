import array
my_arr=array.array('u',["A","B","C","D"]) #u->unicode
for i in range(len(my_arr)):
    print(my_arr[i])

my_arr2=array.array('d',[1,1.2,2.4,0.2]) #d->decimal
for i in range(len(my_arr)): #-->O(n)
    print(my_arr2[i]) #-->O(1)

#time complexity== O(n)+O(1)=>O(n)
# space complexity is constant no extra space is required-->O(1)