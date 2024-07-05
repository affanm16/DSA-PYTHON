#creating dictionaries
#one way is by using dict constructor
my_dict=dict() #->O(1) as empty,space#->O(1) as empty
print(my_dict)

#by curly braces
my_dict2={}     #->O(1) as empty,space#->O(1) as empty
print(my_dict2)

#constructor
eng_spanish=dict(one='uno',two='dos',three='tres')
print(eng_spanish)

#{}
eng_spanis2={'one':'uno','two':'dos','three':'tres'} #->O(n)
print(eng_spanis2)
