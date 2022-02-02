blocks = int(input("Enter the number of blocks: "))
i = 1
height = 0
while i <= blocks:
    blocks -= i
    if blocks >= 0:
        height += 1
    i += 1
print("The height of the pyramid:", height)