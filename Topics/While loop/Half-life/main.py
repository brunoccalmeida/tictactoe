initial_atoms = int(input())
final_atoms = int(input())

count = 0
current_value = int(initial_atoms)

while current_value >= final_atoms:
    current_value = current_value / 2
    count += 1

period_of_days = 12
print(count * period_of_days)
