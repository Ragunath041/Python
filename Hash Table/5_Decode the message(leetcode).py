key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
alpha = [chr(x) for x in range(97, 123)]
hashing = {}

key_list = [i for i in key if i != " "]
message_list = [i for i in message if i != " "]

for i in range(len(alpha)):
    hashing[alpha[i]] = key_list[i]

decoded_message = ""
for char in message_list:
    if char in alpha:
        decoded_message += hashing[char]
    else:
        decoded_message += char
print(key_list)
print(message_list)
print(decoded_message)
print(hashing)
