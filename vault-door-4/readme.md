Link : https://learn.cylabacademy.org/learning-paths/13/84

Soal ini juga cukup mudah, kita hanya perlu fokus ke baris ini
```java
byte[] myBytes = {
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0142, 0131, 0164, 063 , 0163, 0137, 067 , 065 ,
    '9' , '6' , '0' , '0' , 'a' , 'b' , 'c' , '3' ,
};
```
kita identifikasi setiap 8 isi yang disediakan. Baris pertama (index 0-7) merupakan nilai ascii, sehingga decode nya hanya perlu merubah integer tersebut ke nomor nilai ascii. Di python hanya perlu menggunakan ```chr()```.
lalu untuk indeks ke 8 hingga 15 menggunakan hexadec. Sama seperti sebelumnya, karena python bisa langsung membaca hexadec menjadi angka saat program dijalankan, maka kita gunakan cara yang sama seperti cara pertama. Tinggal ```chr()```.
Dan untuk index ke 16 hingga 23 menggunakan octal. Ya caranya sama seperti hexadec. Python bisa langsung membaca menjadi integer.
Dan untuk baris terakhir tidak perlu diapa apain, itu sudah karakter sebenarnya. Tinggal gabungkan ke empat jawaban. Solusi ditulis pada ```main.py```. Selesaikan sendiri terlebih dahulu
