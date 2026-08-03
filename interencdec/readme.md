Link : https://learn.cylabacademy.org/learning-paths/17/135

Untuk menyelesaikan soal ini, kita harus tahu dulu ciri ciri base64
Ini senangkepku aja, cmiiw
1. Panjang karakter adalah kelipatan 4
2. Diakhiri dengan ```=``` atau ```==```

Karakter dalam ```enc_flag``` cukup sesuai dengan kriteria ini. Perhatikan
```YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==```
Jika kita decode dengan Base64 Decoder, maka hasilnya akan menjadi ini
```b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='```
Perlu kita perhatikan, bahwa hasil decoder belum jelas, namun ada sebuah tanda, yaitu ```==``` pada akhir string. Yang menandakan itu adalah Encoded Base64
