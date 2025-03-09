dict = {
    "suraj" : "Sun",
    "kursi" : "Chair",
    "hawa" : "Air",
    "kitab" : "Book",
    "daravaja" : "Door",
    "awaj" : "Sound"
    }

print("Hindi words: ", dict.keys())

word = input("Enter a word you want meaning of: ")
print(dict.get(word, "Not Found"))