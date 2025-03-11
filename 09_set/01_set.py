s1 = {1,5,2,78,25,3}
s2 = {5,2,4,7,9,36,25,35,45}

s1.add(9)
s1.remove(1)
print(s1)

print(s1.union(s2))
print("Intersection : ", s1 & s2)
print("Difference: ", s1.difference(s2))


# Explanation:
# s.add(22): Adds 22 (an integer) to the set.
# s.add(22.00): Since 22.00 (a float) is numerically equal to 22 (integer), Python treats them as the same value in a set. Therefore, it does not add a new element.
# s.add("22"): "22" is a string, which is different from 22 (integer). Since sets allow heterogeneous types, this gets added.
# Key Concept:
# In Python sets, an integer and its equivalent float are considered the same due to Python's internal number handling.
# However, strings are different from numbers, so "22" is treated as a unique value.
s = set()
s.add(22)
s.add(22.00)
s.add(22.22)
s.add("22")
print(s)