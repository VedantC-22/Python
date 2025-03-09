a = ()
print(a)
print(type(a))

a = (25, 66, "Vedant", 44.23, 'c', True, 66)
print(a)
# a[0] = 23 #tuple's are immutable

print("------count()-------")
countOf66 = a.count(66)
print("Count of 66 is ", countOf66)

n = "Vedant"
#ternary operator
print(a.index(n) if n in a else -1)