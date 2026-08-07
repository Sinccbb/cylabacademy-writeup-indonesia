# Write-up: New Caesar (cylabacademy)

- **Category   :** Cryptography
- **Difficulty :** Medium
- **Author     :** Lim Almadyuni (Limath)
- **Concepts   :** RSA
- **Link       :** https://learn.cylabacademy.org/learning-paths/17/138
---

## Executive Summary
Pada soal RSA ini, kita diberikan beberapa komponen utama enkripsi RSA, yaitu Ciphertext (C), Modulus (N), Public Exponent (e), serta dua faktor prima penyusun N yaitu p dan q. Karena nilai p dan q sudah diketahui, kita tidak perlu melakukan faktorisasi N secara manual/brute-force.Proses dekripsi dilakukan dengan menghitung nilai Totient Euler \phi(N), mencari Private Exponent (d) melalui Modular Inverse, lalu mengembalikan nilai Ciphertext (C) menjadi Message (M). Pada tahap akhir, nilai desimal M dikonversi menjadi urutan byte teks ASCII yang kemudian dibalik (reversed) untuk mendapatkan format flag yang benar.
