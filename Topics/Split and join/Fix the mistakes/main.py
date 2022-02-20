text = input()
words = text.split()
list_of_addresses = [word for word in words if
                     word.lower().startswith(('http://', 'https://', 'www.'))]
for address in list_of_addresses:
    print(address)
