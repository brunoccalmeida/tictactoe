user_input = input().capitalize().split()
list_of_corrected_words = []
for word in user_input:
    if '_' in word:
        user_input.remove(word)
        temp_list = word.split('_')
        for element in temp_list:
            list_of_corrected_words.append(element.capitalize())
            new_word = "".join(list_of_corrected_words)
        user_input.append(new_word)

for e in user_input:
    print(e)
