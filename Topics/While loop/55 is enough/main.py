list_of_numbers = []
count = 0
total_sum = 0
number = 0
break_factor = 55

while True:
    number = int(input())
    if number == break_factor:
        break
    list_of_numbers.append(number)
    total_sum += number
    count += 1

# for number in list_of_numbers:
#     print(number)

average = round(total_sum / count)
print(count)
print(total_sum)
print(average)
