mixed_list = [1, "hello", 3.14, True]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]
print(mixed_list[:2])

#deletion

#pop()
print(mixed_list.pop())
print(mixed_list.pop(1)) #2nd element will be removed
#delete()
del numbers[1]
print(numbers)
#remove()

numbers.remove('2')
print(numbers)