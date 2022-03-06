lst1 = [1,2,3,4]
lst2 = lst1
# We wanna change an element of lst2. It will change the element of lst1 too.
lst2[1] = 'Helll'
print(lst1)
######################3
lst3 = [1,2,3,4,5,6]
lst4 = lst3[:] #Copying a list
lst4[1] = 'Hell'
print(lst3)
print(lst4)
########################
#COPYING SOME ELEMENTS FROM A LIST...........
newList = lst3[1:3]
print(newList)
print(lst3)
################# Slicing from start to end(without specifying start)................
mylist = [1,2,3,4,5]
newlist = mylist[:2]
print(newlist)
################# Slicing from Start to end (without specifying end)...........
mylist1 = [1,2,3,4,5]
newlist1 = mylist1[3:]
print(newlist)
################# Deleting using slices..................
my_list2 = [10, 8, 6, 4, 2]
del my_list2[1:3]
print(my_list2)