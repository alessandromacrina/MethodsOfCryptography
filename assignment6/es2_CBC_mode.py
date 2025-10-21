# Funzione per convertire un numero in un carattere Unicode
def number2letter(d):
    # Converte un byte (0-255) in un carattere Unicode
    return chr(d)

# Funzione di iterazione della Feistel
def f(r, k):
    # La funzione di iterazione F(r,k) = (r & k) ^ ((k % 16) | r)
    return (r & k) ^ ((k % 16) | r)

# Una singola iterazione Feistel su un blocco [L,R]
def iter(M, k, f):
    r = M[1]           # prendi il lato destro
    l = M[0] ^ f(r, k) # calcola il nuovo lato sinistro usando XOR con F(r,k)
    return [r, l]      # restituisci il nuovo blocco [R,L] (swap incluso)

# Decifrazione di un blocco Feistel con più iterazioni
def feistel_block_decrypt(M, keys, f):
    block = M.copy()
    # Applica le chiavi in ordine inverso (come richiede la decrittazione Feistel)
    for k in reversed(keys):
        block = iter(block, k, f)
    return block  # restituisce [R,L] finale

# -----------------------------
# Dati: ciphertext, chiavi e IV
ciphertext = [[33, 212], [65, 246], [39, 176], [56, 197], [94, 243], [36, 175], [34, 194], [87, 242],
              [47, 184], [41, 218], [80, 235], [43, 183], [44, 218], [93, 251], [33, 191], [43, 198],
              [83, 250], [45, 190], [41, 203], [65, 235], [42, 166], [54, 200], [67, 230], [54, 161],
              [50, 198], [91, 249], [40, 180], [40, 223], [72, 226], [53, 162], [57, 216], [84, 238],
              [52, 190], [39, 208], [70, 235], [59, 160], [53, 208], [69, 248], [57, 162], [50, 219],
              [64, 249], [62, 177], [40, 216], [88, 234], [49, 190], [61, 212], [79, 241], [52, 168],
              [56, 217], [78, 238], [46, 168], [51, 217], [92, 227], [43, 168], [43, 199], [70, 251],
              [32, 181], [81, 237]]
keys = [161, 2, 214]  # le tre chiavi per le iterazioni Feistel
IV = [53, 160]        # Initialization Vector per CBC

# -----------------------------
# Decifrazione in modalità CBC
prev_block = IV       # inizializziamo prev_block con l'IV
plain_text_str = ''   # stringa finale per contenere il plaintext

for block in ciphertext:
    # Decifra il blocco con Feistel (3 iterazioni)
    r, l = feistel_block_decrypt(block, keys, f)  # ritorna [R,L]
    decrypted_block = [l, r]                        # inverti per ottenere [L,R] reale
    # Applica CBC XOR: Plain[i] = Decipher(Cipher[i]) XOR Cipher[i-1]
    plain_block = [decrypted_block[0] ^ prev_block[0],
                   decrypted_block[1] ^ prev_block[1]]
    # Converti i due byte in caratteri e aggiungi al plaintext
    plain_text_str += number2letter(plain_block[0]) + number2letter(plain_block[1])
    # Aggiorna prev_block con il blocco cifrato corrente
    prev_block = block

# Stampa il plaintext completo
print(plain_text_str)
