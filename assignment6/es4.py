def f(r, k):
    return (r&k)^((k%16)|r)

def iter_block(M, k, f):
    r = M[1]
    l = M[0] ^ f(r, k)
    return [r, l]

def feistel_encrypt_block(M, keys, f):
    block = M.copy()
    for k in keys:
        block = iter_block(block, k, f)
    return block

def feistel_decrypt_block(M, keys, f):
    # applica gli iter con le chiavi in ordine inverso
    block = M.copy()
    for k in reversed(keys):
        block = iter_block(block, k, f)
    return block

def number2letter(d):
    return chr(d)

# Dati 
keys = [161, 2, 214]
ciphertext = [[71, 87], [80, 73], [70, 67], [77, 82], [68, 67], [77, 66], [71, 80], [77, 71], [72, 67], [66, 91], [93, 77], [90, 93], [80, 73], [71, 64], [79, 95], [66, 76], [85, 87], [69, 85], [83, 85], [84, 80], [77, 90], [65, 89], [71, 64], [75, 69], [94, 91], [69, 95], [91, 87], [70, 80], [68, 62]]


#  CTR decryption
plaintext = ''
for i, block in enumerate(ciphertext):
    # contatore per il blocco i: a = F(i, chiave_primo_round)
    a = f(i, keys[0])          # i parte da 0 (block number)
    counter_block = [a, a]
    # cifriamo il contatore usando la procedura di decryption della rete Feistel
    keystream = feistel_decrypt_block(counter_block, keys, f)

    # XOR elemento per elemento
    p0 = block[0] ^ keystream[0]
    p1 = block[1] ^ keystream[1]

    # ricomponi le due lettere (ordine : prima p0 poi p1)
    plaintext += number2letter(p0) + number2letter(p1)

print("Plaintext decifrato:")
print(plaintext)
