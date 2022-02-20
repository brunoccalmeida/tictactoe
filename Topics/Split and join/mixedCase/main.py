sentence = input().split()

for i, word in enumerate(sentence):
    if i == 0:
        continue
    sentence[i] = word.capitalize()

print("".join(sentence))
