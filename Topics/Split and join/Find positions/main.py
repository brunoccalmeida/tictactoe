sequence_numbers = input().split()
number_x = input()
list_of_index = [index for index, value in enumerate(sequence_numbers) if value == number_x]
if list_of_index:
    for item in list_of_index:
        print(item, end=" ")
else:
    print('not found')
