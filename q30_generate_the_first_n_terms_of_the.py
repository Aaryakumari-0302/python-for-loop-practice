# Question 30: Generate the first n terms of the series 1, 4, 9, 16, 25, ...

n = int(input("Enter number of terms: "))
for i in range(1, n + 1):
    print(i * i, end=" ")
print()
