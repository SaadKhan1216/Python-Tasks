## Question
for i in range(-1,1):
   print('#')

## Question
i = 2
while i >=0:
    print('*')
    i -= 2

## Question
list = [1,2,3,4]
print(list[-3:-2])

## Question
x = 1
x = x == x
print(x)

## Question
list1 = [1,2,3]
list2= []
for v in list1:
    list2.insert(0,v)
print(list2)

## Question
i = 0
while i<=3:
    i+=2
    print('*')

## Question
t = [[3-i for i in range(3)] for j in range(3)]
s= 0
for i in range(3):
    s += t[i][i]
print(s)

## Question
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e)

## Question
list = [[0,1,2,3] for i in range(2)]
#print(list[2][0])

## Question
z= 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

## Question
print(0 % 2)

## Question
list = [1,2,3]
for v in range(len(list)):
    list.insert(1,0)
print(list)

## Question
print('--------------------')
var = 1
while var < 10:
    print('#')
    var = var << 1

## Question
vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(sum(vals))

## Question
var = 0
while var < 6:
    var +=1
    if var%2 == 0:
        continue
    print('#')

## Question
for i in range(1):
    print('#')
else:
    print('#')

## Question
vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)