teams = [[f"A-{i}", f"B-{i}"] for i in range(1, 12)]
team_members = [word for words in teams for word in words]
terminated = False
cards = input().split()
for card in cards:
    if card in team_members:
        team_members.remove(card)
        if str(team_members).count("A-") < 7 or str(team_members).count("B-") < 7:
            terminated = True
            break

print(f"Team A - {str(team_members).count('A-')}; Team B - {str(team_members).count('B-')}")
if terminated:
    print("Game was terminated")