count = 0

while True:
    sample_float = input()
    if sample_float == '.':
        break
    sample_float = float(sample_float)
    if count == 0:
        minimum = sample_float
    if sample_float < minimum:
        minimum = sample_float
    count = 1

print(minimum)
