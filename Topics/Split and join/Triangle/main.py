triangle_height = int(input())
multiplier = 1
size = triangle_height * 2

for _ in range(0, triangle_height):
    print(f'{"#" * multiplier:^{size}}')
    multiplier += 2
