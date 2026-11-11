# Question 25: Remove duplicate values from a list while preserving their order.

numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique)
