# for loops

# print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in range(2,6):
    print(x)

for x in range(2, 30, 3):
    print(x)


# the else keyword in a for loop secifies a block of code to be executed when the loop is finished:


for x in range(6):
    print(x)
else:
    print("finished")

# note : the else block will not be executed if the loop is stopped by a break statement.

for x in range(6):
    if x == 3: break 
    print(x)
else:
    print("finished")
    

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
