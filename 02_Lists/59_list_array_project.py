#creating a project using arrays/list
#goal: step-1: take the input as number of days
#step-2: take the temperature for each day
#step-3: calculate the average of the input temperature 
#step-4: now calculate the no of days  which have temp greater than average temp

def calculate_temp():
    no_of_days=int(input("input number of days "))
    temp_list=[]
    for i in range(1,no_of_days+1):
        temp=int(input(f'input the temperature value for day{i}:  '))
        temp_list.append(temp)
    avg=sum(temp_list)/no_of_days
    print(f'average temperature is:{avg}')
    l2=[item for item in temp_list if item> avg]
    return print(f'No. of days above average temp are {len(l2)}')

if __name__=='__main__':
    calculate_temp()

