list_of_numbers = [int(x) for x in list(input())]
list_cumulative_sum = [sum(list_of_numbers[:n + 1]) for n in range(len(list_of_numbers))]
print(list_cumulative_sum)
