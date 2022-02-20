numeric_sequence = input()
list_of_numeric_sequence = numeric_sequence.split()
reversed_list = reversed(list_of_numeric_sequence)
for i in reversed_list:
    print(i, end=' ')
