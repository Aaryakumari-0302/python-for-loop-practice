# Question 18: Count how many times the letter 'a' appears in a string.

text = "banana and apple are amazing"
count = 0
for ch in text:
    if ch == 'a':
        count += 1
print("Letter 'a' appears", count, "times")
