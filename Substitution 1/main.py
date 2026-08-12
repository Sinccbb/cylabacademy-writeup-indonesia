encrypt = "abcdefghijklmnopqrstuvwxyz"
message = "aipfhrswmoxqdkjulgybzntevc"
lower_message = message.lower()
lower_encrypt = encrypt.lower()
upper_message = message.upper()
upper_encrypt = encrypt.upper()
dekrip = str.maketrans(lower_encrypt + upper_encrypt, lower_message + upper_message)

mess = input("Masukkan pesan yang ingin didekripsi: ")

print("\nHasil Dekripsi :\n" +mess.translate(dekrip))