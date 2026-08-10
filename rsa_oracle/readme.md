# Write-up: [rsa_oracle]() cylabacademy

- **Category   :** Cryptography
- **Difficulty :** Medium
- **Author     :** Geoffrey Njogu
- **Written by :** Lim Almadyuni (Limath)
- **Concepts   :** RSA
---

## Executive Summary
Disini, flag tersimpan dalam ```secret.enc```, dan saat kita buka menggunakan kode dibawah
```python
with open("secret.enc", "rb") as f:
    encrypted_secret = f.read()

print(encrypted_secret)
```
kita dapat melihat hasilnya 
```
b'Salted__jX\xc1\xef\xf39V)\xe1pT3\xcf\xbeq\xfb\x03$\xaaqEs\xfc5\xb6n\\K5=\xc1%c\xba\xb3\t\xdcQ\xd39s\xba\x1a\x0e1!quM\xfe0\x8d\x954\xaa\x87'
```
dan jika kita coba buka dengan
```shell
openssl enc -d -aes-256-cbc -in secret.enc -out secret.txt
```
kita akan dimintai password, maka tugas kita adalah mendecode ```password.txt```, jika kita jalankan ```nc titan.picoctf.net <port>```, dan masukkan ```password.enc```, maka tidak muncul apa apa. Sebelumnya, aku pengen kasih tau ini dulu, kan 
$$C \equiv M^e mod N$$
dan
$$M \equiv C^d mod N$$
Dengan 
C = Udah diekripsi
M = Pesan asli
e = kunci enkripsi
d = kunci dekripsi
Oracle gak dibolehin untuk decrypt password.enc secara langsung, maka kita bisa akalin bikin pesan enkripsi palsu lewat oracle
misal enkripsi "2", nanti kita kalikan hasil enkripsi "2" dan password dan namain C_palsu, lalu setelah selesai, dekripsi C_palsu tersebut, lalu dekripsi dengan The Oracle, dan rubah hasilnya ke int, lalu bagi dengan "2" tadi, solusi dapat dilihat pada solve.py, lalu masukkan password saat menjalankan 

```shell
openssl enc -d -aes-256-cbc -in secret.enc -out flag.txt
```
nanti flagnya ada di file ```flag.txt```