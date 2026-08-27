# Write-up: [Password Profiler](https://learn.cylabacademy.org/library/712?page=3&difficulty=1&workspace=true) (cylabacademy)

- **Category   :** General Skills
- **Difficulty :** Medium
- **Author     :** Darkraicg492
- **Written by :** Lim Almadyuni (Limath)
---
## Executive Summary
Soal ini cukup simpel tapi melelahkan, karena password di enkripsi menggunakan SHA1 yang dimana sifat enkripsinya hanya satu arah dan tidak bisa di decrypt. Saat melihat hint, ternyata kita diarahkan untuk menggunakan tool di github bernama cupp. Kita tinggal download
```ssh
git clone https://github.com/Mebus/cupp.git
```
setelah itu nanti kita coba jalankan
```ssh
python3 cupp.py -i
```
dan masukkan beberapa informasi yang disediakan. Nanti tool ini akan melakukan generate kode berdasarkan info tersebut. Cukup lama, saya bahkan menunggu kurang lebih 10 menitan. Setelah itu, kita sesuaikan nama file nya dari ```alice.txt``` menjadi ```passwords.txt```. Dan tinggal jalanin ```checkpassword.py```
## Flag
```picoCTF{Aj_15901990}```
