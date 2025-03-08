l = ["Apple", "Grapes", 5, 3.2, False, "Vedant"]
print(l)

nums = [12,8,89,55,31,4,2,57,44]

#List methods
nums.sort()
# nums.reverse()

nums.append(10)

nums.insert(2, 50)
print(nums)

#Accepting fruit names from user
# l = []
# for i in range(0, 7):
#     fruit = input("Enter fruit name: ")     
#     l.append(fruit)

# print(l)


### **4️⃣ Rotate a List Left by `k` Positions**
li = [1, 2, 3, 4, 5]
res = li[2:] + li[0: 2]
print(res)