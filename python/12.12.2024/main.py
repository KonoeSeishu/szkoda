#cw 5
text = "Python good good lang"
words = text.split(" ")
print(words)
result = []

for idx, word in enumerate(words): #return index + value from list
    if idx < 4:
        result.append(word.lower()) #only small letters
print(result)

#cw 6
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result1 = []

for prob in probabilities:
    if prob >= 0.5:
        result1.append(1)
    else:
        result1.append(0)
print(result1)

#cw 7
text2 = """"All cats are cute, uwu"""
words = text.split()
print(words)

for word in words:
    word = [word.replace(",", "").replace(".", "") for word in words]

print(words)