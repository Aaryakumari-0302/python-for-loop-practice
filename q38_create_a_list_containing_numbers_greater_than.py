# Question 38: Create a list containing numbers greater than 10 from an existing list.

numbers = [4, 11, 25, 8, 15, 10, 30]
result = []
for n in numbers:
    if n > 10:
        result.append(n)
print(result)
