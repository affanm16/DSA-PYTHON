# class StarCookie:
#     def __init__(self,color,size):
#         self.color=color
#         self.size=size
        


# star_cookie1=StarCookie()
# star_cookie1.weight=15
# star_cookie1.colpor="red"
# print(star_cookie1.weight)
# star_cookie2=StarCookie()
# star_cookie2.weight=20
# star_cookie2.color='blue' 


class Youtuber:
    def __init__(self,username,subscribers=0,subscriptions=0):
        self.username=username
        self.subscribers=subscribers
        self.subscriptions=subscriptions

    def subscribe(self,user):
        user.subscribers+=1
        self.subscriptions+=1




user1=Youtuber("mohammad")
user2=Youtuber("affan")
user1.subscribe(user2)
print(user1.subscribers)
print(user2.username)
print(user1.subscriptions)
print(user2.subscriptions)


