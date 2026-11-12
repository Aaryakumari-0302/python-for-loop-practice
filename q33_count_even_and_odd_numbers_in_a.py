# Question 33: Count even and odd numbers in a list.

numbers = [3, 8, 15, 22, 7, 10, 41, 6]
even = odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
