# A fibonacci series is a series such that every number is the sum of the two proceding ones.

our_number = int(input('Enter a number to proceed: '))


def fib(n):
    a = 0
    b = 1
    count = 0
    empty_list =[]

    #Check if the introduced integer is valid
    if n <= 0:
        print("Incorrect input, enter a positive integer")

    elif n == 1:
        print(b)

    else:
        while count < n:
            #We append each value of the fibonacci series to an empty list in order to print it later
            empty_list.append(a)
            nth = a + b
            #Update values
            a = b
            b = nth
            count += 1
        print("The total sum for {} elements of fibonacci series is: {}".format(n, sum(empty_list)))


fib(our_number)


