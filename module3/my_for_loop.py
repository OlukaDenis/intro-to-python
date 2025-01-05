counter = [1,2,3,4,5,6,7,8,9,10]
item = 1

# For loop condition
# For loops work with a sequenc of items
# this include; list, tuple, range
for item in counter:
    print('Counter: ', item)

    # if item == 3:
    #     continue

    # if item == 3:
    #     break

    if item % 2 == 1:
        print('Odd Number: ',item)
    # Counting up and increasing counter's value by 1 in each iteration
    item += 1 

# This is a nested loop

# for i in range(1, 4):
#     print('i = ', i)
#     for j in range(4):
#         print('j = ', j)
#         print('i * j: ', i * j)
