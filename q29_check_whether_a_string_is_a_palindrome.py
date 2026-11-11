# Question 29: Check whether a string is a palindrome using a for loop.

text = input("Enter a string: ")
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not a palindrome")
