import string

enc_flag = "fegdeogdgecoeocgcgchcfcffccfca"
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(text):
    dec = ""
    for i in range(0, len(text), 2):
        temp = ""
        c1 = text[i]
        c2 = text[i + 1]
        binary1 = "{0:04b}".format(ALPHABET.index(c1))
        binary2 = "{0:04b}".format(ALPHABET.index(c2))
        temp += binary1 + binary2
        dec += chr(int(temp, 2))
    return dec

def shift(c, k):
    t1 = ALPHABET.index(c)
    t2 = ALPHABET.index(k)
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

def shift_text(s, k):
    dec = ""
    for i in s:
        dec += shift(i, k)
    return dec
    
# 2. Lakukan shift DULU, baru b16_decode!
for i, j in enumerate(ALPHABET):
    b16_text = shift_text(enc_flag, j)  # Geser mundur dulu
    flag = b16_decode(b16_text)           # Baru decode b16
    print(f"Nyoba ke {i} (Key '{j}') = "+"picoCTF{"+flag+"}")