def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result

for i in range(1, 26):
    encrypted_text = caesar_cipher("dspttjohuifsvcjdpohatwvibg", i)
    print("Shift : "+str(i) +" = picoCTF{"+encrypted_text+"}")