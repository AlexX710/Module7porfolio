#Alex Flores
#November 7, 2023
#Problem 4 Unique
# The code will take a list of numbers and return a new list.

list = [1, 3, 3, 3, 6, 2, 3, 5]

res_list = []

for item in list:
    if item not in res_list:
        res_list.append(item)
for item in res_list:
    print(item)