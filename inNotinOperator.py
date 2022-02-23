my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

###### Finding Greater Element..
my_list1 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list1[0]

for i in range(1, len(my_list1)):
    if my_list1[i] > largest:
        largest = my_list1[i]

print(largest)