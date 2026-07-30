Soal ini cukup simpel, yaitu kita tinggal membalik hal yang sudah diacak acak oleh program
```Java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb4c_u_4_m2r640");
    }
```
anggap aja jawaban benar tersimpan di ```password[]```, lalu diacak dan encoded password ada pada ```buffer[]```. Kita hanya tau apa isi ```buffer[]```, tapi kita juga sudah mengetahui proses encode nya. Maka kita bisa membalik proses itu untuk mendapat jawaban asal.

