def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    decoded_words = []
    position = 1

    for line in lines:
        words = line.split()
        decoded_words.append(words[position])
        position += 1

    return ' '.join(decoded_words)

# Provide the filename containing the encoded message
message_file = "encoded_message.txt"
decoded_message = decode(message_file)
print(decoded_message)
