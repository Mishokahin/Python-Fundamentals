morse_code_values = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
                     "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
                     "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
                     "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

morse_code = [code.strip() for code in input().split(' | ')]
message = []

for idx in range(len(morse_code)):
    message.append("".join([morse_code_values[character] for character in morse_code[idx].split()]))

print(" ".join(message))