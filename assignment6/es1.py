# Funzione per convertire un numero in un carattere Unicode
def number2letter(d):
    return chr(d)

# Funzione di iterazione per la decrittazione
def iter(M, k, f):
    r = M[1]
    l = M[0] ^ f(r, k)
    return [r, l]

# Funzione di decrittazione di un blocco
def feistel_block_decrypt(M, keys, f):
    block = M.copy()
    for k in reversed(keys):  # Le chiavi devono essere usate in ordine inverso
        block = iter(block, k, f)
    return block

# Funzione per la funzione di iterazione
def f(r, k):
    return (r & k) ^ ((k % 16) | r)

# Dati di input
M = [[2, 76], [11, 64], [6, 86], [17, 80], [16, 74], [11, 71], [23, 70], [10, 66], [3, 80], [22, 70], [0, 70], [29, 87], [21, 83], [0, 77], [12, 66], [8, 76], [13, 70], [16, 77], [1, 75], [22, 68], [17, 76], [0, 77], [1, 78], [10, 66], [0, 80], [23, 76], [27, 87], [21, 83], [23, 79], [0, 76], [1, 76], [26, 80], [29, 87], [23, 87], [10, 76], [29, 87], [17, 77], [0, 70], [28, 87], [12, 70], [22, 76], [17, 80]]
keys = [161, 2, 214]

# Decifrazione del testo
plain_text = []
# Ricostruzione corretta del plaintext leggibile
plain_text_str = ''
for block in M:
    l, r = feistel_block_decrypt(block, keys, f)
    plain_text_str += number2letter(r) + number2letter(l)  # invertiamo l'ordine qui
print(plain_text_str)


# Unione dei caratteri decifrati in una stringa
plain_text_str = ''.join(plain_text)
print(plain_text_str)
