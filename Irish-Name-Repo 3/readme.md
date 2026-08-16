# Write-up: [Irish-Name-Repo 3](https://learn.cylabacademy.org/learning-paths/7/66) (cylabacademy)

- **Category   :** Web Exploitation
- **Difficulty :** Medium
- **Author     :** Xingyang Pan
- **Written by :** Lim Almadyuni (Limath)
---

## Executive Summary
Coba kita menggunakan SQL Injection dulu yaitu ```' OR 1=1 --```, dan nanti hasilnya akan seperti ini.
<img src="Screenshot/1.png">
Dapat diketahui bahwa web ini dapat diretas menggunakan SQL Injection biasa, tapi seharusnya sudah selesai kan? Kok ini gak nampilin flag? Oke jadi kita baca hint nya dulu. ```Seems like the password is encrypted.```, brarti passwordnya dienkripsi, maka dari itu, kita perlu tahu apa jenis enkripsi yang digunakan
## Flag
```picoCTF{3v3n_m0r3_SQL_2af58a67}```
