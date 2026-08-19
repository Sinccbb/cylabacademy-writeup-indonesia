# Write-up: [ABSOLUTE NANO](https://learn.cylabacademy.org/library/748?page=1&difficulty=2&category=5&workspace=true) (cylabacademy)

- **Category   :** General Skills
- **Difficulty :** Medium
- **Author     :** Darkraicg492
- **Written by :** Lim Almadyuni (Limath)
---
## Executive Summary
Di soal ini, kita hanya disuruh baca ```flag.txt```, cuma saat kita ```cat``` atau ```nano```, gak muncul apa apa karena gak ada akses buat pemula, yang punya akses cuma sepuh. Dan saat kita ```sudo``` untuk menjadi sepuh, maka akan dimintai password yang tentunya kita gak tau passwordnya apa karena masih pemula. Okey, coba lihat yang memiliki akses siapa aja dengan menjalankan ```sudo -l```. Nah ternyata ada sesuatu kerentanan ```(ctf-player ALL=(ALL) NOPASSWD: /bin/nano /etc/sudoers)``` nih, ktia bisa pura pura jadi sepuh dengan menggunakan jalur ```/bin/nano /etc/sudoers```. Maka dari itu aku buka ```nano``` versi sepuh dengan ```sudo /bin/nano /etc/sudoers```, terus aku klik ```Ctrl+R```, dan aku masukkin directory tempat flag berada, kebetulan sebelumnya udah kujalanin ```pwd```, jadi tinggal masukkin directory ```/home/ctf-player/flag/txt```, dan BOOM dapet flagnya 
## Flag
```picoCTF{n4n0_411_7h3_w4y_7a258d4b}```
