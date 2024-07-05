myDict={'name': 'affan', 'age': 21, 'address': 'hyd'}

#linear Search
def linear_search(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
        else:
            return 'value not found'
print(linear_search(myDict,'affan'))