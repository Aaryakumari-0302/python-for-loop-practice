# Question 36: Print all vowels present in a given string.

text = "Programming in Python"
for ch in text:
    if ch.lower() in "aeiou":
        print(ch)
