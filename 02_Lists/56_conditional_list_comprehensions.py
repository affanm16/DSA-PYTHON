
#example1
l1=[1,2,-3,0,-23,-4,59,-10]
l2=[i**2 for i in l1 if i<0]
print(l2)

#example2

sentence='My name is mohammed affan'
def is_consonant(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.lower() not in vowels

# print(is_consonant('c'))
l2=[i for i in sentence if is_consonant(i)]
print(l2)