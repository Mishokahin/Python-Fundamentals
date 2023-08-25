key = int(input())
message_length = int(input())
message = [chr(ord(input())+key) for i in range(message_length)]

print(*message, sep="")