print("Homework 5. Task 4. Realize RLE algorithm: data compression and decompression")
print()

text = "AAABBBccccCCCCQQQQQ"
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


# DECODE

decoded = ''
count = ''
for char in encoded:
    if char.isdigit():
        count += char
    else:
        decoded += char * int(count)
        count = ''

print("Decoded text:", decoded)