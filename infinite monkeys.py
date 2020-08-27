import random
from urllib.request import urlopen

text = urlopen('http://composingprograms.com/shakespeare.txt').read().decode()

letters = set( letter for word in text.split() for letter in word)
print(letters)

length = len(text)

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
