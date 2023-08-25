number_of_players = int(input())
party_members = {}

for player in range(number_of_players):
    stats = input().split()
    party_members[stats[0]] = {"HP": int(stats[1]), "MP": int(stats[2])}

while True:
    command = input()
    if command == "End":
        break
    command_args = command.split(" - ")
    action = command_args[0]
    if action == "CastSpell":
        hero_name = command_args[1]
        MP_needed = int(command_args[2])
        spell_name = command_args[3]
        if party_members[hero_name]["MP"] < MP_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            party_members[hero_name]["MP"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {party_members[hero_name]['MP']} MP!")

    if action == "TakeDamage":
        hero_name = command_args[1]
        damage = int(command_args[2])
        attacker = command_args[3]
        if party_members[hero_name]["HP"] - damage <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            del party_members[hero_name]
        else:
            party_members[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {party_members[hero_name]['HP']} "
                  f"HP left!")
    if action == "Recharge":
        hero_name = command_args[1]
        amount = int(command_args[2])
        amount_recovered = amount
        if party_members[hero_name]["MP"] + amount > 200:
            amount_recovered = 200 - party_members[hero_name]["MP"]
        party_members[hero_name]["MP"] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")

    if action == "Heal":
        hero_name = command_args[1]
        amount = int(command_args[2])
        amount_recovered = amount
        if party_members[hero_name]["HP"] + amount > 100:
            amount_recovered = 100 - party_members[hero_name]["HP"]
        party_members[hero_name]["HP"] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")

for hero, attributes in party_members.items():
    print(hero)
    print(f" HP: {party_members[hero]['HP']}")
    print(f" MP: {party_members[hero]['MP']}")