# Question 39: Count how many marks in a list are passing marks (40 or above).

marks = [35, 78, 40, 22, 91, 39, 65]
passed = 0
for m in marks:
    if m >= 40:
        passed += 1
print("Passing marks:", passed)
