text = input()

for idx in range(len(text)):
    character = text[idx]
    if character == ":" and idx + 1 < len(text):
        emoticon = text[idx+1]
        print(f":{emoticon}")
        idx += 1