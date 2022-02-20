name_list = []
while True:
    name = input()
    if name == ".":
        break
    name_list.append(name)

print(name_list)
print(len(name_list))
