# Question 28: Count uppercase letters, lowercase letters, and digits in a string.

text = "Hello World 2026 Python3"
upper = lower = digits = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
