import array
my_arr=array.array('i',[10,20,30,40]) #i->integer
print(my_arr)
my_arr.insert(0,900)
print(my_arr)
my_arr.insert(4,786)
print(my_arr)
my_arr.insert(1000,99) #what ever the index positon(here 1000),if it is greater than the last value,the value will be inserted at the end
print(my_arr)

#time complexity
# as insertion requires shifting of n values(n operations) so
# worst case senior inserting at position 0-->n operations ==> O(n)
# space compexity will be O(1) => as 1 place is required 
