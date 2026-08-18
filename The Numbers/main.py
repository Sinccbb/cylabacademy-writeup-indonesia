acong = "16 9 3 15 3 20 6 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14"
split_cong = acong.split(" ")
angka = [int(i) for i in split_cong]
flag = [chr(i + 96) for i in angka]
print("".join(flag))