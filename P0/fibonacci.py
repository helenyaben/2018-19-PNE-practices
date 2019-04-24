# A fibonacci series is a series such that every number is the sum of the two proceding ones.

our_number = int(input('Enter a number to proceed: '))

def fib(n):
    a = 0
    b = 1
    count = 0

    #Check if the introduced integer is valid
    if n <= 0:
        print("Incorrect input, enter a positive integer")

    elif n == 1:
        print(b)

    else:
        while count < n:
            print(a, end=',')
            nth = a + b
            #Update values
            a = b
            b = nth
            count += 1

print("The fibonacci series of {} elements is: ".format(our_number), end='')
fib(our_number)

