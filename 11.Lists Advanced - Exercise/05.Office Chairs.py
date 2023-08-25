n = int(input())
halls = list(input().split() for i in range(n))
check = list(bool(j[0].count("X") >= int(j[1])) for i, j in enumerate(halls))
chairs = list(j[0].count("X") for i, j in enumerate(halls))
guests = list(int(j[1]) for i, j in enumerate(halls))

if all(check):
    print(f"Game On, {sum(chairs) - sum(guests)} free chairs left")
else:
    print("\n".join(f"{guests[i] - chairs[i]} more chairs needed in room {i + 1}"
                    for i, j in enumerate(check) if not j))