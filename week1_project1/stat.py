import math

user_list = input("Enter in numbers separated by a space: ")

split_variable = user_list.split()

list_numbers = []
for numbstring in split_variable:
    integer = int(numbstring)
    list_numbers.append(integer)

n = len(list_numbers)

print("Your list of numbers is: "  ,list_numbers)

mmm = input("Would you like the find the mean, median, or mode? ")

if mmm == "mean":
    print("The mean is: ",sum(list_numbers)/n)


if mmm == 'median':

    x = sorted(list_numbers)
    y = len(x)

    if y % 2 == 0:
        r = math.floor(y / 2)
        w = math.ceil( y / 2)
        s = (r+w) / 2
        print("The median is: ", s)

    else:
        z = math.floor(y / 2)
        print("The median is: ", x[z])

if mmm == 'mode':
    d = {}
    for key in list_numbers:
        if key in d:
            d[key] += 1
        else: 
            d[key] = 1

    greatest_value =  0 
    greatest_key = None

    for key in d:
        if d[key] > greatest_value:
            greatest_key = key
            greatest_value = d[key]
    
    print("The mode is: ", greatest_key)


    # d = {x:list_numbers.count(x) for x in list_numbers}
    # print(max(d, key=d.get))

