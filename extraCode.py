import random
import sys
#sys.exit()

text = ""
with open("RosGuil.txt", "r") as file:
	text = file.read()
	collection = set()
	for letter in text:
		collection.add(letter)
	print(collection)

letters = ['m', '-', 'G', 'J', 'A', 'f', 'N', 'j', 'w', 'Q', 'r', 'e', 'i', 'Z', 'â', 'a', 'I', 'T', 'z', 'B', 'g', 'd', '.', 'L', ',', 'x', '/', '!', ' ', 'p', "'", 'b', 't', ')', 'v', 'R', '"', 'O', 'U', '“', 'Y', 'k', 'y', 'E', '€', 'K', 'h', 'W', 'C', 'q', 'F', 'D', 'o', '(', 'H', ';', 'l', '?', 'n', '\n', 'S', 's', 'c', 'P', 'u', ':', 'M', 'V']

for letter in letters:
	print(f"{letter}", text.find(letter))

length = len(text)
print(length)

attempt = ""
count = 0
while True:
    for i in range(length):
        attempt += random.choice(letters)
    if attempt == text:
        print("huzza")
        print(count)
        break
    else:
        attempt = ""
        count += 1