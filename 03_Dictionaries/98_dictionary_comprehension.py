import random
city_names=['hyderabad','mumbai','delhi','chennai']
new_dict={city:random.randint(28,30) for city in city_names}
print(new_dict)

#create a dict from it where it has the cities which have temp greater than 29
city_temps={city:temp for (city,temp) in new_dict.items() if temp>29}
print(city_temps)
