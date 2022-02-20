n = int(input())
list_of_winners = []
for _ in range(n):
    player, win_or_loss = input().split()
    if win_or_loss == 'win':
        list_of_winners.append(player)
# list_of_players = [(player, win_or_loss) for _ in range(n)]
# list_of_winners = [element[0] for element in list_of_players if element[1] == 'win']
print(list_of_winners)
print(len(list_of_winners))
