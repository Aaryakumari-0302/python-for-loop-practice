# Question 27: Merge two equal-length lists by adding their elements at matching positions.

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
merged = []
for i in range(len(list1)):
    merged.append(list1[i] + list2[i])
print(merged)
