
s = "Vedavneat"
#reversing string s
print(s[::-1])

#removing duplicates (non-case sensitive)
set1 = set(s.lower())
print(set1)


str = input("Enter a string: ")
l = str.split(" ")
res = []
for item in l:
    res.append(item[::-1]) 
print(" ".join(res))

