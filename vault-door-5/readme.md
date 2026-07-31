link : https://learn.cylabacademy.org/learning-paths/13/85

langsung aja fokus pada 
```java
public boolean checkPassword(String password) {
    String urlEncoded = urlEncode(password.getBytes());
    String base64Encoded = base64Encode(urlEncoded.getBytes());
    String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    + "JTM0JTVmJTM0JTMyJTYzJTM2JTM0JTMwJTM5JTYy";
    return base64Encoded.equals(expected);
}
```
dari
```java
    String urlEncoded = urlEncode(password.getBytes());
```
dan
```java
    String base64Encoded = base64Encode(urlEncoded.getBytes());
```
kita bisa tahu bahwa flag di encode menjadi url encode, lalu di encode lagi menggunakan base64. Jadi yang kita perlukan hanya membalik, decode dengan base64, lalu dengan url decode
kita bisa membuat program penyelesaiannya seperti pada ```main.py``` atau gunakan saja decoder online seperti https://encoding.tools/