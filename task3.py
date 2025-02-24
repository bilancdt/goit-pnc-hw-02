def vigenere_encrypt(text, key):
    """
    Шифру Віженера.
    """
    key = key.upper()
    text = text.upper()
    encrypted = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            encrypted += char

    return encrypted

def vigenere_decrypt(text, key):
    """
    Дешифр Віженера.
    """
    key = key.upper()
    text = text.upper()
    decrypted = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted += char

    return decrypted

def table_encrypt(text, key):
    """
    Шифрування за допомогою табличного шифру.
    """
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    columns = len(key)
    rows = (len(text) + columns - 1) // columns
    table = [text[i:i + columns] for i in range(0, len(text), columns)]

    if len(table[-1]) < columns:
        table[-1] = table[-1].ljust(columns)

    encrypted = ""
    for col in key_order:
        for row in table:
            encrypted += row[col]

    return encrypted

def table_decrypt(text, key):
    """
    Дешифрування за допомогою табличного шифру.
    """
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    columns = len(key)
    rows = len(text) // columns

    col_lengths = [rows] * columns
    table = ["" for _ in range(columns)]
    index = 0

    for col in key_order:
        table[col] = text[index:index + col_lengths[col]]
        index += col_lengths[col]

    decrypted = ""
    for row in range(rows):
        for col in range(columns):
            if row < len(table[col]):
                decrypted += table[col][row]

    return decrypted.strip()

def encrypt_vigenere_then_table(text, vigenere_key, table_key):
    """
    Шифрування спочатку шифром Віженера, потім табличним шифром.
    """
    vigenere_encrypted = vigenere_encrypt(text, vigenere_key)
    table_encrypted = table_encrypt(vigenere_encrypted, table_key)
    return table_encrypted

def decrypt_vigenere_then_table(text, vigenere_key, table_key):
    """
    Дешифрування спочатку табличним шифром, потім шифром Віженера.
    """
    table_decrypted = table_decrypt(text, table_key)
    vigenere_decrypted = vigenere_decrypt(table_decrypted, vigenere_key)
    return vigenere_decrypted

# Приклад використання
vigenere_key = "MATRIX"
table_key = "CRYPTO"
plaintext = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."

# Шифр
ciphertext = encrypt_vigenere_then_table(plaintext.replace(" ", ""), vigenere_key, table_key)
print("Зашифрований текст:", ciphertext)

# Дешифр
decrypted_text = decrypt_vigenere_then_table(ciphertext, vigenere_key, table_key)
print("Розшифрований текст:", decrypted_text)
