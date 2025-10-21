def number2letter(d):
    return chr(d)

def f(r, k):
    return (r & k) ^ ((k % 16) | r)

def iter(M, k, f):
    r = M[1]
    l = M[0] ^ f(r, k)
    return [r, l]

def feistel_block_encrypt(M, keys, f):
    # In CFB si usa il Feistel in modalità "encrypt" (le chiavi in ordine normale)
    block = M.copy()
    for k in keys:  # ordine normale per cifrare
        block = iter(block, k, f)
    return block  # ritorna [R,L]

# Dati
ciphertext = [[117, 216], [72, 185], [59, 168], [115, 205], [75, 163], [34, 161],
              [113, 194], [87, 188], [60, 177], [115, 218], [92, 178], [35, 190],
              [118, 201], [75, 176], [54, 173], [122, 212], [85, 170], [59, 191],
              [127, 209], [86, 177], [36, 177], [112, 200], [90, 164], [63, 182],
              [102, 188]]
keys = [161, 2, 214]
IV = [53, 160]

prev_block = IV
plain_text_str = ''

for block in ciphertext:
    # Cripta il prev_block con Feistel
    r, l = feistel_block_encrypt(prev_block, keys, f)
    feistel_out = [l, r]  # inverti per ottenere [L,R]
    # XOR con il ciphertext corrente per ottenere il plaintext
    plain_block = [block[0] ^ feistel_out[0], block[1] ^ feistel_out[1]]
    plain_text_str += number2letter(plain_block[0]) + number2letter(plain_block[1])
    # Aggiorna prev_block con il ciphertext corrente
    prev_block = block

print(plain_text_str)
