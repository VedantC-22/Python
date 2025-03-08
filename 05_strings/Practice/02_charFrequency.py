from collections import Counter

def calculateFreq(str):
    freq = Counter(str.replace(" ", ""))
    max = 0
    char = ''
    for item, f in freq.items():
        if max < f:
            max = f
            char = item
        print(f"{item}: {f}")
    print("Most frequenct char is ", char)
    
# str = input("Enter a string: ")
# calculateFreq(str)


#Another method
def calculateFreq2(str):
    d = {}
    for char in str:
        if char in d.keys():
            d[char] += 1
        else:
            d[char] = 1
    
    print(d)

str = "Vadfadf"
calculateFreq2(str)