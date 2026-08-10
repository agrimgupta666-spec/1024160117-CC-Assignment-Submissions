# Assingment 1.1: WAP to print your name three times
print("Agrim")
print("Agrim")
print("Agrim")


# Assingment 2.1: WAP to add three numbers and print the result.
a = 10
b = 220
d = 210
c = a + b + d
print(a, " + ", b, " + ", d, " --> ", c)


# Assingment 2.2: WAP to concatinate three strings and print the result.
p = "Aman"
q = "raman"
r = "Hi"
s = p + q + r
print(p, " + ", q, " + ", r, " ---> ", s)


# Assingment 4.1: WAP to print the table of 7, 9.
for i in range(1, 11):
    print(7, " * ", i, " = ", i * 7)

for i in range(1, 11):
    print(9, " * ", i, " = ", i * 9)


# Assingment 4.2: WAP to print the table of n and n is given by user.
a = int(input("Enter Number: "))
for i in range(1, 11):
    print(a, " * ", i, " = ", i * a)


# Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
a = int(input("Enter number: "))
sum = 0

for i in range(1, a + 1):
    sum = sum + i

print("Sum: ", sum)


# Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

d = max(a, b, c)

print("Max: ", d)


# Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n = int(input("Enter Number: "))
sum = 0

for i in range(1, n + 1):
    if(i % 7 == 0 and i % 9 == 0):
        sum = sum + i

print("Sum: ", sum)


# Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n = int(input("Enter a No: "))
sum = 0

for j in range(2, n + 1):
    f = 0

    for i in range(2, j // 2 + 1):
        if j % i == 0:
            f = 1
            break

    if f == 0:
        sum = sum + j

print("Sum: ", sum)


# Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
def doSumOfOdd(n):
    sum = 0

    for i in range(1, n + 1):
        if(i % 2 != 0):
            sum = sum + i

    print("Sum: ", sum)


n = int(input("Enter number: "))
doSumOfOdd(n)


# Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n is given by the user.
def doSumOfPrime(n):
    sum = 0

    for j in range(2, n + 1):
        f = 0

        for i in range(2, j // 2 + 1):
            if j % i == 0:
                f = 1
                break

        if f == 0:
            sum = sum + j

    print("Sum: ", sum)


n = int(input("Enter number: "))
doSumOfPrime(n)