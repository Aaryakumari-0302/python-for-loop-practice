# Question 26: Find the second-largest distinct number in a list without using sort().

numbers = [12, 45, 7, 89, 45, 56, 89]
largest = None
second = None
for n in numbers:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif n != largest and (second is None or n > second):
        second = n
print("Second largest =", second)
