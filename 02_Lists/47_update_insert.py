numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

#updating
numbers[2]=200
print(numbers)

#insertion
# method-1 insert() -inserts an element at any position
mixed_list.insert(0,'hi')
print(mixed_list)

# append()
mixed_list.append('hyd')
print(mixed_list)

#extend() to add another list

mixed_list.extend([10,20,'a','b'])
print(mixed_list)