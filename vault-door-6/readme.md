Link : https://learn.cylabacademy.org/learning-paths/13/86

Perhatikan ini
```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x61, 0x37, 0x65, 0x61, 0x65, 0x65, 0x64,
        };
```
coba kita lihat output dari myBytes
```python
    mbg = [
        0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
        0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
        0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
        0xa , 0x61, 0x37, 0x65, 0x61, 0x65, 0x65, 0x64,
    ]
    print(mbg)
```
```output
[59, 101, 33, 10, 56, 0, 54, 29, 10, 61, 97, 39, 17, 102, 39, 10, 33, 29, 97, 59, 10, 45, 101, 39, 10, 97, 55, 101, 97, 101, 101, 100]
```
Lalu coba perhatikan ini
```java
    for (int i=0; i<32; i++) {
        if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
            return false;
        }
    }
    return true;
```
brarti kita hanya butuh ```(passBytes[i] ^ 85) - myBytes[i]``` bernilai ```0```, atau kita harus mencari ```passBytes[i]``` dimana ```(passBytes[i] ^ 85) = myBytes[i]```. Mari kita lihat tabel xor
```bash
A xor B = C
1     1 = 0
0     1 = 1
1     0 = 1
0     0 = 0
```
anggap kita punya sebuah operasi ```X``` untuk mencari nilai A jika hanya diketahui B dan C saja
```bash
C  x  B = C
0     1 = 1
1     1 = 0
1     0 = 1
0     0 = 0
```
dan ternyata x sama dengan xor, maka kita bisa simpulkan ```passBytes[i] = (myBytes[i] ^ 85)```
solusi sudah tertulis di ```main.py```, intip nanti aja :)