from re import sub

name = input()


def normalize(name_inside):
    new_name = name_inside
    new_name = sub("[éë]", 'e', new_name)
    new_name = sub('[áå]', 'a', new_name)
    new_name = sub('œ', 'oe', new_name)
    return sub('æ', 'ae', new_name)


print(normalize(name))
