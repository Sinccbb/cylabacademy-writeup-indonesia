# Write-up: [Irish-Name-Repo 1](https://learn.cylabacademy.org/learning-paths/7/64) (cylabacademy)

- **Category   :** Web Exploitation
- **Difficulty :** Easy
- **Author     :** Chris Hensler
- **Written by :** Lim Almadyuni (Limath)
---

## Executive Summary
Soal ini adalah soal eksploitasi web yang umum, yaitu mengenai SQL Injection, format umum dari SQL injection tuh simpel, seperti ini
```mysql
SELECT * FROM users WHERE username = '$user' AND password = '$password';
```
brarti kita bisa akalin dengan membuat input yang bisa keluar dari kurungan, kita ganti ```$password``` dengan ```' OR '1'='1``` atau sebagainya yang bisa membuat nilai kebenaran menjadi true. Karena AND akan menjadi prioritas diatas OR, kita juga harus cermat memilih operasi. Contoh jika kita masuk ke ```$user```, kita bisa ganti ```' OR 1=1 OR'```. Nanti akan muncul Login Succes, script kode? gak ada ya, ini tinggal login kok.
## Flag
```picoCTF{s0m3_SQL_85832275}```
