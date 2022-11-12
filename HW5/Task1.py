print("Homework 5. Task 1. Delete all words that include characters 'abc'", 
        "from given text")
print()


text = "Ekd, lqp ajboc eowbc caodb qeab, bbc, pcba. Bddasc iqicx, aaebc!"
excluding = 'abc'
excluding = excluding.lower() # ...just in case
text_lst = text.split()

print("Given text:")
print(text)
print()

print("Place of words with 'abc':")
j = 0
for i in range(len(text_lst)):
    scan = text_lst[j].lower()
    if excluding[0] in scan and excluding[1] in scan and excluding[2] in scan:
        print(i, ' - ', scan)
        if ',' in scan:
            text_lst[j] = ','
        elif '.' in scan:
            text_lst[j] = '.'
        elif '!' in scan:
            text_lst[j] = '!'
        elif '?' in scan:
            text_lst[j] = '?'
        else:
            del text_lst[j]
            j -= 1
    j += 1



print()
result_text = " ".join(text_lst)
print("Corrected text: \n" + result_text)