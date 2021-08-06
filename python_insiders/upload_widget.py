text = "Hello How are you doing?"

text_split = text.split()

for word in text_split:
    for letter in word:
        print(letter)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


thisdict["color"] = 0

print(thisdict)
