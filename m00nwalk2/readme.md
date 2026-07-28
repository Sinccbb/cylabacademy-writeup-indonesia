Link : https://learn.cylabacademy.org/learning-paths/8/68
Flagnya disembunyikan dengan teknik steganografi pada ```message.wav```, untuk decode steganografi, diperlukan password yang bisa didapatkan melalui ```clue1.wav```, tidak perlu pedulikan ```clue2.wav``` dan ```clue3.wav```. Dapatkan password dengan decode ```clue1.wav``` menggunakan SSTV decoder, lalu password yang muncul, gunakan untuk membuka ```message.wav``` menggunakan 
```bash
steghide extract -sf message.wav
```