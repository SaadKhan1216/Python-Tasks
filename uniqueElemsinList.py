my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
new_list = []
# Write your code here.
for num in my_list:
    if num not in new_list:
        new_list.append(num)
print("The list with unique elements only:")
print(new_list)