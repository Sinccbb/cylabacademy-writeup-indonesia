# Write-up: Safe Opener(cylabacademy)

- **Category   :** Safe Opener Series
- **Difficulty :** Mediun
- **Author     :** Mubarak Mikail
- **Written by :** Lim Almadyuni (Limath)
- **Concepts   :** Reverse Engineering
- **Link       :** [Safe Opener](https://learn.cylabacademy.org/learning-paths/10/74)
---

## Executive Summary
Perhatikan Kode ini
```Java
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
```
Untuk tahu itu jenis enkripsi apa, kita lihat kode diatasnya
```Java
Base64.Encoder encoder = Base64.getEncoder();
```
Oke jadi tinggal buka [Base64 Decoder](https://www.base64decode.org/), dan ya udah ketemu passwordnya, tinggal bungkus pake picoCTF{}


Flag :```picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}```