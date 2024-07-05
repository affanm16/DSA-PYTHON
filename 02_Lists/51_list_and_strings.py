a="spam"
b=list(a)
print(b)

a="spam spam spam and ham"
b=a.split()
print(b)

a="spam spam spam and ham"
b=a.split('a')
print(b)


a="spam-spam1-spam2-spam3"
delimiter='-'
b=a.split(delimiter)
print(b)
print(delimiter.join(b))