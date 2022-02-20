text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

user_input = int(input())
list_of_words = [word for a_list in text for word in a_list if len(word) <= user_input]
print(list_of_words)
