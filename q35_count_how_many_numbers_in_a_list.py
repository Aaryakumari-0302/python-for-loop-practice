# Question 35: Count how many numbers in a list are greater than 50.

numbers = [10, 55, 72, 49, 90, 50, 61]
count = 0
for n in numbers:
    if n > 50:
        count += 1
print("Numbers greater than 50:", count)
