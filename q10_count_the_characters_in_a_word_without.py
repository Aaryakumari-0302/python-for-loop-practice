# Question 10: Count the characters in a word without using len().

word = input("Enter a word: ")
count = 0
for ch in word:
    count += 1
print("Number of characters =", count)
