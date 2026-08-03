import base64

import base64
enc = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg=="
dec = base64.b64decode(enc.encode("utf-8"))
res = dec.decode("utf-8")

enc = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=="
dec = base64.b64decode(enc.encode("utf-8"))
res = dec.decode("utf-8")

def caesar_chiper(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result
for shift in range(1, 27):
    decrypted_text = caesar_chiper(res, shift)
    print(f"Shift {shift}: {decrypted_text}")