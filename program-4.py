def playfair_cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper().replace("J", "I")
    key = key.upper().replace("J", "I")

    key_table = []

    for letter in key:
        if letter not in key_table:
            key_table.append(letter)

    for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letter not in key_table:
            key_table.append(letter)

    key_table = [key_table[i:i+5] for i in range(0, 25, 5)]

    print("Key Matrix:")
    for row in key_table:
        print(row)
    plaintext_pairs = []
    i = 0

    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i+1]
            if a != b:
                plaintext_pairs.append(a + b)
                i += 2
            else:
                plaintext_pairs.append(a + "X")
                i += 1
        else:
            plaintext_pairs.append(a + "X")
            i += 1
    print("Pairs:", plaintext_pairs)
    def find_position(letter):
        for r in range(5):
            for c in range(5):
                if key_table[r][c] == letter:
                    return r, c
    ciphertext = ""
    for pair in plaintext_pairs:
        letter1, letter2 = pair[0], pair[1]
        row1, col1 = find_position(letter1)
        row2, col2 = find_position(letter2)
        if row1 == row2:
            ciphertext += key_table[row1][(col1 + 1) % 5]
            ciphertext += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_table[(row1 + 1) % 5][col1]
            ciphertext += key_table[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_table[row1][col2]
            ciphertext += key_table[row2][col1]
    return ciphertext
plaintext = "HELLO WORLD"
key = "example"
ciphertext = playfair_cipher(plaintext, key)
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
