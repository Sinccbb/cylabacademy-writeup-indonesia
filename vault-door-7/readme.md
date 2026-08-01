Link : https://learn.cylabacademy.org/learning-paths/13/87


Tantangan ini meminta kita untuk menemukan password 32 karakter untuk membuka pintu vault (`VaultDoor7`). Password dipotong menjadi 8 bagian, di mana tiap bagian terdiri dari 4 karakter ASCII yang digabungkan (*packed*) menjadi satu buah bilangan bulat 32-bit (`int`).

Pada method `passwordToIntArray`, 4 byte karakter digabungkan menjadi 1 buah `int` menggunakan kombinasi *left shift* (`<<`) dan *bitwise OR* (`|`):

```java
x[i] = hexBytes[i*4]     << 24
     | hexBytes[i*4+1]   << 16
     | hexBytes[i*4+2]   << 8
     | hexBytes[i*4+3];
```
ASCII itu 8 bit, maka anggap aja 
```plaintext
hb[  4*i  ] = aaaaaaaa
hb[4*i + 1] = bbbbbbbb
hb[4*i + 2] = cccccccc
hb[4*i + 3] = dddddddd
```
maka 
```plaintext
x[i] = aaaaaaaa bbbbbbbb cccccccc dddddddd
```
lihat, tidak ada bit yang berubah sama sekali, brarti kita tinggal balikkan aja shift nya tanpa meduliin or tadi
maka didapatkan
```plaintext
hb[  4*i  ] = x[i] >> 24
hb[4*i + 1] = x[i] >> 16
hb[4*i + 2] = x[i] >> 8
hb[4*i + 3] = x[i]
```
Tapi tunggu, operasi itu masih menyisakan bit tetangga, maka kita harus memusnahkan dengan identitasnya
```plaintext
hb[  4*i  ] = (x[i] >> 24) & 255
hb[4*i + 1] = (x[i] >> 16) & 255
hb[4*i + 2] = (x[i] >> 8 ) & 255 
hb[4*i + 3] = (x[i]      ) & 255    
```
dan perhatika ini
```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734292070
            && x[6] == 825440356
            && x[7] == 858796849;
    }
```
yups, kita udah dikasih x nya, yaudah tinggal eksekusi