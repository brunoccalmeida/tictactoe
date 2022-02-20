text = input()


def remove_special_symbols(text_sample):
    new_text = text_sample
    return new_text.strip("*_~`")


if __name__ == '__main__':
    print(remove_special_symbols(text))
