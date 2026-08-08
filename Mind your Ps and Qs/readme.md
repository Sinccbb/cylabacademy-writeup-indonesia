# Write-up: Mind your Ps and Qs (cylabacademy)

- **Category   :** Cryptography
- **Difficulty :** Medium
- **Author     :** Lim Almadyuni (Limath)
- **Concepts   :** RSA
- **Link       :** https://learn.cylabacademy.org/learning-paths/17/138
---

## Executive Summary
Pada soal RSA ini, kita diberikan beberapa komponen utama enkripsi RSA, yaitu Ciphertext (C), Modulus (N), Public Exponent (e), serta dua faktor prima penyusun N yaitu p dan q. Karena nilai p dan q sudah diketahui, kita tidak perlu melakukan faktorisasi N secara manual/brute-force.Proses dekripsi dilakukan dengan menghitung nilai Totient Euler $\phi(N)$, mencari Private Exponent (d) melalui Modular Inverse, lalu mengembalikan nilai Ciphertext (C) menjadi Message (M). Pada tahap akhir, nilai desimal M dikonversi menjadi urutan byte teks ASCII yang kemudian dibalik (reversed) untuk mendapatkan format flag yang benar.

Catatan Tambahan Untuk RSA : 

**1. Pembentukan Kunci (Key Generation)**

Sebelum enkripsi dan dekripsi dapat dilakukan, pasangan kunci publik (Public Key) dan kunci privat (Private Key) harus dibuat melalui langkah-langkah berikut:

- **Pemilihan Bilangan Prima :** Pilih dua bilangan prima rahasia berukuran besar $p$ dan $q$.
  
- **Perhitungan Modulus $N$ :** Hitung nilai $N$ yang akan digunakan sebagai batas modulus operasi: $$N = p \times q$$ 

- **Perhitungan Totient Euler $\phi(N)$ :** Hitung nilai fungsi totient untuk $N$ : $$\phi(N) = (p - 1) \times (q - 1)$$

- **Pemilihan Eksponen Enkripsi $e$ :** Pilih nilai $e$ (umumnya $e = 65537$) dengan syarat $e$ relatif prima terhadap $\phi(N)$ : $$\gcd(e, \phi(N)) = 1$$

- **Perhitungan Eksponen Dekripsi $d$ :** Hitung $d$ yang merupakan Modular Multiplicative Inverse dari $e$ modulo $\phi(N)$ : $$d \equiv e^{-1} \pmod{\phi(N)} \quad \text{atau} \quad (e \times d) \equiv 1 \pmod{\phi(N)}$$

- **Public Key:** $(e, N)$ — Boleh dipublikasikan untuk mengunci pesan.

- **Private Key:** $(d, N)$ atau $(p, q, d)$ — Wajib dirahasiakan untuk membuka pesan.


**2. Proses Enkripsi**

Proses pengubahan pesan asli $M$ (Plaintext) menjadi ciphertext $C$ dilakukan oleh pengirim menggunakan Public Key $(e, N)$.
- **Konversi Pesan:** Pesan teks $M$ diubah terlebih dahulu menjadi bentuk nilai integer $M$ dengan syarat $0 \le M < N$.
- **Formula Enkripsi:** Ciphertext $C$ dihitung menggunakan eksponensiasi modular: $$C = M^e \pmod N$$


**3. Proses Dekripsi**

Proses mengembalikan ciphertext $C$ menjadi pesan asli $M$ dilakukan oleh penerima menggunakan Private Key $(d, N)$.
- **Formula Dekripsi:** Integer pesan $M$ diperoleh kembali melalui perhitungan: $$M = C^d \pmod N$$ 
- **Konversi Kembali :** Nilai integer $M$ selanjutnya dikonversi dari bentuk angka/byte kembali menjadi teks ASCII/UTF-8 asli.
