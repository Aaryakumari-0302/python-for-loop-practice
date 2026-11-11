# Question 12: Calculate the sum of the digits of a positive integer.

n = int(input("Enter a positive integer: "))
total = 0
for digit in str(n):
    total += int(digit)
print("Sum of digits =", total)
