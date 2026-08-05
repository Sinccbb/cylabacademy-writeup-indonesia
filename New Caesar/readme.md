# Write-up: New Caesar (cylabacademy)

- **Category   :** Cryptography
- **Difficulty :** Easy / Medium
- **Author     :** Lim Almadyuni (Limath)
- **Concepts   :** Base16 Custom Encoding, Caesar Cipher (Modulo Arithmetic), Brute-Force Key Space
- **Link       :** https://learn.cylabacademy.org/learning-paths/17/136
---

## Executive Summary
Perhatikan kode ini
```py
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
```
Simpelnya kode tersebut akan merubah ke kode ascii, dirubah ke biner, dipisah jadi 4 bagian awal dan 4 bagian akhir, lalu dirubah kedua biner baru itu ke desimal, lalu desimal akan dirubah ke anggota ```ALPHABHET = "abcdefghijklmnop"```

contoh seperti ini

```plaintext
encode
a = 97 (in ASCII)
01100001
0110 0001 = 6 1 = g b (in ALPHABET)
```

Maka, untuk merubah menjadi bentuk asal, kita hanya perlu membalik logika nya. Dibutuhkan kelipatan jumlah karakter kelipatan 2 untuk decode nya. Lalu kita rubah masing masing huruf menjadi desimal berdasarkan index ALPHABET, lalu ke biner, dan menyatukan biner itu dan merubah ke desimal untuk dikonversi menjadi ascii. Gambarannya gini

```plaintext
decode
g = 6 = 0110 (in ALPHABET)
b = 1 = 0001 (in ALPHABET)
"0110" + "0001" = "01100001" 
int("01100001",2) = 97
chr(97) = a
```

maka didapatkan decoder seperti ini
```python
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
```

untuk tes apakah berhasil, maka tinggal panggil aja
```print(b16_decode(b16_encode("a")))```
```output
a
```

dan ternyata decodernya berhasil. Lanjut

Sekarang fokus ke kode ini
```python 
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
```

dimana pemain utamanya adalah

```python
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```

ini sebenernya pergeseran biasa, k sebagai penggesernya, yang dimana misal ```k = 'a'```, maka digeser 0 kekanan. ```k = 'b'``` digeser 1 kali ke kanan. Biar lebih percaya, coba jalankan kode ini.
karena keluarannya banyak, gak akan kutampiln disini

```python
import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

for i in ALPHABET:
    for j in ALPHABET:
        print(f"Percobaan {i} digeser dengan {j} : {shift(i, j)}")
```

Lalu kode ini

```python
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
```
sebenernya ada yang perlu kita rubah dikit, yaitu syarat agar tidak error adalah ```len(key) == 1```, lalu ```key``` harus anggota ```ALPHABET``` (a s/d p).

pada kode 
```python
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
```
sebenernya pergeseran juga hanya 1 karakter, dan yang diambil adalah karakter ke pertama saja (karena juga ```len(key)``` harus 1). Shingga bisa dimodif

```python
flag = "redacted"
key = "redacted"
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[0])
```
Dan sifat pergeseran ini akan berputar, sehingga kita gak perlu membuat algoritma unshift. Dan kalo mentok bisa lihat solusi di ```main.py```, jangan kaget, salah satu dari yang ada adalah flag.