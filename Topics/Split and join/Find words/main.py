words = input().split()
ends_with_s = [word for word in words if word.endswith('s')]
new_string = "_".join(ends_with_s)
print(new_string)
