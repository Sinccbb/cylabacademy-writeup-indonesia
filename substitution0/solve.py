ukey = "DECKFMYIQJRWTZPXGNABUSOLVH"
lkey = ukey.lower()
lwc = "abcdefghijklmnopqrstuvwxyz"
upc = lwc.upper()
decryptor = str.maketrans(ukey + lkey, upc + lwc)
enc = input("Enter the encrypted text: ") 
print("Decrypted text: " + enc.translate(decryptor))