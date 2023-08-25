import re

number_of_messages = int(input())

attacked_planets = []
destroyed_planets = []

for message in range(number_of_messages):
    encrypted_message = input()

    key_pattern = r"[S,T,A,R,s,t,a,r]"
    encryption_key = len(re.findall(key_pattern, encrypted_message))

    decrypted_message = "".join([chr(ord(char) - encryption_key) for char in encrypted_message])
    search_pattern = r".*(\@[a-zA-Z]+)([^\@\-\!\:\>]*?)(:[0-9]+)([^\@\-\!\:\>]*?)(![A-Z]!)([^\@\-\!\:\>]*?)(->[0-9]+)"
    data = re.search(search_pattern, decrypted_message)
    if data:
        plannet = data.group(1)[1:]
        attack_destruction = data.group(5)[1]
        if attack_destruction == "A":
            attacked_planets.append(plannet)
        else:
            destroyed_planets.append(plannet)

print(f"Attacked planets: {len(attacked_planets)}")
attacked_planets.sort()
for attacked in attacked_planets:
    print("-> " + attacked)
print(f"Destroyed planets: {len(destroyed_planets)}")
destroyed_planets.sort()
for destroyed in destroyed_planets:
    print("-> " + destroyed)