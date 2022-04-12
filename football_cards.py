team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

terminated = False

cards = input().split()

for player in range(len(cards)):
    if cards[player] in team_a:
        team_a.remove(cards[player])
        if len(team_a) < 7:
            terminated = True
            break
    elif cards[player] in team_b:
        team_b.remove(cards[player])
        if len(team_b) < 7:
            terminated = True
            break
    else:
        continue

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated:
    print("Game was terminated")


#     cards = input().split()
#     # split_cards = list(cards.split("-"))
#     if cards[0] in team_a:
#         team_a.remove(cards[0])
#         if len(team_a) < 7:
#             terminated = True
#             break
#         else:
#             continue
#     elif cards[0] in team_b:
#         team_b.remove(cards[0])
#         if len(team_b) < 7:
#             terminated = True
#             break
#     else:
#         continue
