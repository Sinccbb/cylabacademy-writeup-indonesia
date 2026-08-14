# Write-up: [Irish-Name-Repo 2](https://learn.cylabacademy.org/learning-paths/7/65) (cylabacademy)

- **Category   :** Web Exploitation
- **Difficulty :** Easy
- **Author     :** Chris Hensler
- **Written by :** Lim Almadyuni (Limath)
---

## Executive Summary
Aku udah nyobain beberapa kombinasi SQL Injection, tapi yaa gagal, dan aku iseng iseng nyoba satu logika ini, pada umumnya, kita bisa login jika username dan password yang kita masukkan benar, dan biasanya username dari admin ya "admin", sedangkan passwordnya gak tau, jadi aku nyari gimana cara agar dia ini cuma butuh username aja, akhirnya aku kepikiran dengan cara comment. Dalam SQL, komentar tuh (--) untuk satu baris setelah tanda tersebut, dan (/* text */) untuk yang berada didalam komen. Maka aku akalin untuk menghilangkan baris setelah user
## Flag
```picoCTF{}```
