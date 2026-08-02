Kalo kalian lihat kode ini, pasti males
```Java
    // These pesky special agents keep reverse engineering our source code and then
    // breaking into our secret vaults. THIS will teach those sneaky sneaks a
    // lesson.
    //
    // -Minion #0891
    import java.util.*; import javax.crypto.Cipher; import javax.crypto.spec.SecretKeySpec;
    import java.security.*; class VaultDoor8 {public static void main(String args[]) {
    Scanner b = new Scanner(System.in); System.out.print("Enter vault password: ");
    String c = b.next(); String f = c.substring(8,c.length()-1); VaultDoor8 a = new VaultDoor8(); if (a.checkPassword(f)) {System.out.println("Access granted."); }
    else {System.out.println("Access denied!"); } } public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
    char[] a = password.toCharArray(); for (int b=0; b<a.length; b++) {char c = a[b]; c = switchBits(c,1,2); c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ c = switchBits(c,5,6); c = switchBits(c,4,7);
    c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ c = switchBits(c,3,4); c = switchBits(c,2,5); c = switchBits(c,6,7); a[b] = c; } return a;
    } public char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit
    that was in position p2 to position p1. Precondition: p1 < p2 */ char mask1 = (char)(1 << p1);
    char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ char bit1 = (char)(c & mask1); char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
    System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ char rest = (char)(c & ~(mask1 | mask2)); char shift = (char)(p2 - p1); char result = (char)((bit1<<shift) | (bit2>>shift) | rest); return result;
    } public boolean checkPassword(String password) {char[] scrambled = scramble(password); char[] expected = {
    0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0xB4, 0xC1, 0xA5, 0xF1, 0xC2, 0xD1, 0xF0, 0xF1 }; return Arrays.equals(scrambled, expected); } }
```
Jadi ya satu-satunya cara ya kita simpelkan aja, ya "simpelkan aja" kode ini. Walau sebenernya bisa pake AI, cuma disini aku simpelkan secara manual. Hal yang kulakukan adalah
1. Beresin kode, biar gak jadi satu baris gitu, kita pisah pisah barisnya berdasarkan titik koma.
2. Ini yang aku baru tau, fungsi dalam java tuh boleh gak urut. Tentu kita gak terbiasa jika sebelumnya sering pake Python, C++, C, dll. Makanya aku juga balik urutannya biar lebih sesuai dengan kebiasaan aja. Disitu kan fungsi ```scramble()``` ditaruh sebelum ```switchBits()```. Padahal ```switchBits()``` sudah digunakan pada ```scramble()```
3. Disitu kebanyakan operasi sampah yang ditaruh komen, jadi komen komen gak berguna itu aku hapus aja

Dan didapatkan kode berikut
```java
    // These pesky special agents keep reverse engineering our source code and then
    // breaking into our secret vaults. THIS will teach those sneaky sneaks a
    // lesson.
    //
    // -Minion #0891
    import java.util.*;
    import javax.crypto.Cipher;
    import javax.crypto.spec.SecretKeySpec;
    import java.security.*;
    class VaultDoor8 {public static void main(String args[]) {
        Scanner b = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String c = b.next();
        String f = c.substring(8,c.length()-1);
        VaultDoor8 a = new VaultDoor8();
        if (a.checkPassword(f)) {
            System.out.println("Access granted.");
        }
        else {
            System.out.println("Access denied!");
        } 
    } 
    public char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit that was in position p2 to position p1. Precondition: p1 < p2 */ 
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2);
        char bit1 = (char)(c & mask1);
        char bit2 = (char)(c & mask2);
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1<<shift) | (bit2>>shift) | rest);
        return result;
    } 
    public char[] scramble(String password) {
        /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray();
        for (int b=0;b<a.length;b++) {
            char c = a[b];
            c = switchBits(c,1,2);
            c = switchBits(c,0,3);
            c = switchBits(c,5,6);
            c = switchBits(c,4,7);
            c = switchBits(c,0,1);
            c = switchBits(c,3,4);
            c = switchBits(c,2,5);
            c = switchBits(c,6,7);
            a[b] = c;
        }
        return a;
    } 
    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password);
        char[] expected = { 0xF4, 0xC0, 0x97, 0xF0, 0x77, 
                            0x97, 0xC0, 0xE4, 0xF0, 0x77, 
                            0xA4, 0xD0, 0xC5, 0x77, 0xF4, 
                            0x86, 0xD0, 0xA5, 0x45, 0x96, 
                            0x27, 0xB5, 0x77, 0xE0, 0xB4, 
                            0xC1, 0xA5, 0xF1, 0xC2, 0xD1, 
                            0xF0, 0xF1 };
        return Arrays.equals(scrambled, expected); 
    } }
```
Lebih bersih kan? oke, fokus selanjutnya adalah penyelesaian. Yang perlu kita ketahui adalah, fungsi ```scramble()``` adalah algoritma utamanya, sedangkan ```switchBits()``` adalah algoritma pembantu yang dimana kita hanya perlu mendecode ```scramble()```. Ya agar lebih mudah bayanginnya, kayak algoritma ```sort()``` dan ```swap()```. Disitu ```swap()``` hanya membantu untuk menukarkan saja. Ya tapi jangan samain ```scramble()``` sama ```sort()```, soalnya ```sort()``` ini bersifat satu arah aja, gak bisa di decode. Untuk mendecode ```scramble()```, kita hanya perlu membalik urutannya dari bawah ke atas aja. Lalu ```switchBits()``` itu bisa di decode dengan dirinya sendiri. Jadi pemanggilan ```switchBits()``` dua kali akan membatalkan penukaran yang pertama. Seperti ```swap()``` yang jika dia dipanggil untuk kedua kali, maka akan kembali ke bentuk awal. Buka solusi di ```main.py``` kalo udah mentok aja.