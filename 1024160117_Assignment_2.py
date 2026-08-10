# Q1: Lists

roll_no = "1024160117"

# Extract digits and multiply each digit by 10
L = []

for i in roll_no:
    L.append(int(i) * 10)

print("Original List:", L)


# ii. Add two numbers using append() and insert()

L.append(50)
print("After append:", L)

L.insert(2, 70)
print("After insert:", L)


# iii. Remove two elements using remove() and pop()

L.remove(50)
print("After remove:", L)

L.pop()
print("After pop:", L)


# iv. Sort ascending and descending

L.sort()
print("Ascending:", L)

L.sort(reverse=True)
print("Descending:", L)


# v. Slicing first three and last three elements

print("First three elements:", L[:3])
print("Last three elements:", L[-3:])


# vi. List comprehension greater than average

average = sum(L) / len(L)

new_list = [x for x in L if x > average]

print("Elements greater than average:", new_list)


# Q2: Tuples

scores = tuple(L[:8])

print("Scores tuple:", scores)


# i. Highest score and index

highest = max(scores)
print("Highest score:", highest)
print("Index of highest score:", scores.index(highest))


# Lowest score and count

lowest = min(scores)

print("Lowest score:", lowest)
print("Lowest score appears:", scores.count(lowest), "times")


# ii. Reverse tuple and return as list

# Tuple cannot be reversed directly because tuples are immutable

reverse_scores = list(scores[::-1])

print("Reversed tuple as list:", reverse_scores)


# iii. Search score

x = int(input("Enter score to search: "))

if x in scores:
    print("First occurrence index:", scores.index(x))
else:
    print("Score not present")


# iv. Trying to change tuple

# scores[0] = 100
# Error: TypeError because tuple values cannot be changed


# v. Tuple unpacking

first, second, *remaining = scores

print("First:", first)
print("Second:", second)
print("Remaining:", remaining)


# Q3: Random Numbers

import random

roll_no = 1024160117

# Setting seed
random.seed(roll_no)


# i. Generate list of 100 random numbers

numbers = []

for i in range(100):
    numbers.append(random.randint(100, 900))

print("Random Numbers:")
print(numbers)


# ii. Count and print odd numbers

odd_numbers = []

for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)

print("Odd Numbers Count:", len(odd_numbers))
print("Odd Numbers:", odd_numbers)



# iii. Count and print even numbers

even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers Count:", len(even_numbers))
print("Even Numbers:", even_numbers)



# iv. Count prime numbers and create prime list

def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in numbers if checkPrime(x)]

print("Prime Numbers Count:", len(prime_numbers))
print("Prime Numbers:", prime_numbers)



# v. Number occurring most frequently

frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1


most_common = max(frequency, key=frequency.get)

print("Most frequent number:", most_common)
print("Frequency:", frequency[most_common])


# Q4: Sets

roll_no = "1024160117"

digits = []

for i in roll_no:
    digits.append(int(i))


# Creating sets

A = set()

B = set()

for i in digits:
    A.add(i * 7)
    B.add(i * 9)


print("Set A:", A)
print("Set B:", B)



# vi. Union

print("Union:", A.union(B))


# vii. Intersection

print("Intersection:", A.intersection(B))


# viii. Difference

print("A - B:", A.difference(B))

print("B - A:", B.difference(A))

# difference() gives values present only in one set.
# symmetric_difference() gives values present in either set but not common.



# ix. Symmetric Difference

print("Symmetric Difference:", A.symmetric_difference(B))


# x. Subset and Superset

print("A is subset of B:", A.issubset(B))

print("B is superset of A:", B.issuperset(A))



# xi. Remove value using discard()

x = int(input("Enter value to remove from A: "))

A.discard(x)

print("Set A after discard:", A)


# Q5: Dictionary

my_dict = {
    "name": "Agrim",
    "roll_no": "1024160117",
    "branch": "CSE",
    "age": 21,
    "city": "Dera Bassi"
}


print("Original Dictionary:")
print(my_dict)



# i. Rename city key to location using pop()

my_dict["location"] = my_dict.pop("city")

print("After changing city to location:")
print(my_dict)



# ii. Add cgpa

my_dict["cgpa"] = 7.7

print("After adding CGPA:")
print(my_dict)



# iii. Increase age by 1

my_dict["age"] = my_dict["age"] + 1

print("After updating age:")
print(my_dict)



# iv. Delete branch using pop()

dict1 = my_dict.copy()

removed_branch = dict1.pop("branch")

print("After deleting branch using pop:")
print(dict1)


# Delete branch using del

dict2 = my_dict.copy()

del dict2["branch"]

print("After deleting branch using del:")
print(dict2)


# pop() returns the deleted value, while del only deletes the key.



# v. Iterate using items()

print("Dictionary items:")

for key, value in my_dict.items():
    print(key, "→", value)



# vi. Check email key

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email key does not exist")



# vii. Merge with friend dictionary

friend_dict = {
    "name": "Rahul",
    "roll_no": "1024160123",
    "branch": "ECE",
    "age": 21,
    "city": "Patiala"
}


merged_dict = {**my_dict, **friend_dict}

print("Merged Dictionary:")
print(merged_dict)


# When same key exists, values of second dictionary overwrite first dictionary values.



# viii. Dictionary comprehension for string values

string_dict = {
    key: value 
    for key, value in my_dict.items()
    if isinstance(value, str)
}


print("Dictionary containing only string values:")
print(string_dict)