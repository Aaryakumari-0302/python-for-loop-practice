# Question 13: Count the digits in a positive integer using its string form.

n = int(input("Enter a positive integer: "))
count = 0
for digit in str(n):
    count += 1
print("Number of digits =", count)
