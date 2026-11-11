# Question 21: Reverse a string using a for loop without slicing.

text = input("Enter a string: ")
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print("Reversed:", reversed_text)
