text = input()


def delete_punctuation(a_text):
    text_to_change = a_text.lower()
    return text_to_change.replace(',', '').replace('.', '').replace('!', '').replace('?', '')


print(delete_punctuation(text))
