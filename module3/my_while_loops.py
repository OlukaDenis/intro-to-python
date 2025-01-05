counter = 1

# This is a while loop
# It iterates the counter starting from 1 to 10
# It stops when the counter value reaches 10
while counter <= 10:
    print('Counter: ', counter)
    if counter % 2 == 1:
        print('Odd Number: ',counter)
    # Counting up and increasing counter's value by 1 in each iteration
    counter += 1 
else:
    print('The counter ', counter, ' is greater than 10, so the loop has been stopped.')