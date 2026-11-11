# Question 15: Calculate the average of 5 numbers entered by the user.

total = 0
for i in range(5):
    total += float(input(f"Enter number {i + 1}: "))
print("Average =", total / 5)
