dict = {1: "Vedant", 2: "Dhiraj", 3: "Chetan", 4:"Shivam"}
print(dict)

# accessing dict element
# print(dict[11]) #using this if key is not present in dictionary it throws keyError
print(dict.get(11)) #it will return None if key is not present

#update dict
dict.update({3: "Toukesh", 5: "Dnyanya"}) #it update the value of key which is present, if the key is not present it add that key-value pair to dict.
print(dict)

# dict methods
print(dict.keys()) #dict_keys([1, 2, 3, 4, 5])
print(dict.values()) # dict_values(['Vedant', 'Dhiraj', 'Toukesh', 'Shivam', 'Dnyanya'])
print(dict.items()) # dict_items([(1, 'Vedant'), (2, 'Dhiraj'), (3, 'Toukesh'), (4, 'Shivam'), (5, 'Dnyanya')])

del dict[1]
print(dict)


# Dictionary Comprehension
squares = {x: x**2 for x in range(1, 11)}
print(squares)