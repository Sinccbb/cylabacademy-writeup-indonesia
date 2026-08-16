encoded = "nopqrstuvwxyzabcdefghijklm"
asli = "abcdefghijklmnopqrstuvwxyz"
encoded = encoded + encoded.upper()
asli = asli + asli.upper()
translator = str.maketrans(encoded, asli)
text = " ' OR 1=1 -- "
decoded_text = text.translate(translator)
print(decoded_text)