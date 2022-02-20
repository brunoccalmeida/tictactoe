prime_numbers = [2, 3, 5, 7, 11, 13]
number = 14
prime = True

while number < 1000:
    for n in range(2, (number // 2)):
        if any([number % n == 0]):
            prime = False
            break
        else:
            prime = True
    if prime:
        prime_numbers.append(number)
        number += 1
    else:
        number += 1
