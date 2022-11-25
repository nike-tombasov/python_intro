print("Homework 5. Task 4. Realize RLE algorithm: data compression and decompression")
print()

text = open('orig_text.txt', 'r').read()
print("Original text:", text)


# ENCODE
encoded = ''
prev_char = ''
count = 1

if not text:
    encoded = ''
else:
    for char in text:
        if char != prev_char:
            if prev_char:
                encoded += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoded += str(count) + prev_char

print("Encoded text:", encoded)
with open('encoded.txt', 'w') as data:
    data.writelines(encoded)

# DECODE

with open('encoded.txt', 'r') as data:
    encoded_text = data.read()
decoded = ''
count = ''
for char in encoded_text:
    if char.isdigit():
        count += char
    else:
        decoded += char * int(count)
        count = ''

with open('decoded.txt', 'w') as data:
    data.writelines(decoded)
print("Decoded text:", decoded)