# Write-up: [Safe Opener 2](https://learn.cylabacademy.org/learning-paths/10/75) cylabacademy

- **Category   :** Reverse Engineering
- **Difficulty :** Easy
- **Author     :** Mubarak Mikail
- **Written by :** Lim Almadyuni (Limath)
---

## Executive Summary
Ya aku cukup kaget dengan soal ini, karena ya flagnya tertulis jelas tanpa perlu effort lagi. Dan ternyata gini, ```.class``` adalah ekstensi excecutable dari java, jadi cara kerja java itu adalah compiler dan interpreter sekaligus, ```.java``` kita compile menjadi ```.class```, dan ```.class``` di interpreter sehingga kodenya bisa dibaca. Nah uniknya, di VS Code tuh ```.class``` akan dirubah menjadi kode ```.java``` sehingga akan gampang sekali baca nya. Jika kita buka file yang disediakan pada tantangan secara langsung menggunakan perintah ```cat```, kurang lebih gini hasilnya
```bash
cat SafeOpener.class
```
Output
```class
cat SafeOpener.class 
����4�
CDE     FG
H
I
JL      FN
OP
Q
RS
.T
OU
VW
X
Y
[
]
R`ab<init>()VCodeLineNumberTableLocalVariableTablethis
                                                      LSafeOpener;main([Ljava/lang/String;)VisOpenZargs[Ljava/lang/Stringkeyboard▒Ljava/io/BufferedReader;encodercEncoder
       InnerClasses▒Ljava/util/Base64$Encoder;
StackMapTable*Dcdang/String;keyiI
ExceptionsopenSafe(Ljava/lang/String;)password
SourceFileSafeOpener.java
                         java/io/BufferedReaderjava/io/InputStreamReaderf
                                                                         gh
                                                                           i
                                                                            jk
                                                                              lm
                                                                                noEnter password for the safe: p
                               qr
                                 std
                                    uv
                                      wx
                                        yr
                                          >?java/lang/StringBuilder
You have  
          z{
            z| attempt(s) left
                              }t,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}
                                                                             ~
                                                                              Sesame openPassword is incorrect

SafeOpenerjava/lang/Object▒java/util/Base64$Encoderjava/lang/Stringjava/io/IOExceptionjava/lang/SysteminLjava/io/InputStream;▒(Ljava/io/InputStream;)V(Ljava/io/Reader;)Vjava/util/Base64
getEncoder()Ljava/util/Base64$Encoder;outLjava/io/PrintStream;java/io/PrintStreamprint(Ljava/lang/String;)readLine()Ljava/lang/StringgetBytes()[BencodeToString([B)Ljava/lang/String;printlnappend-(Ljava/lang/String;)Ljava/lang/StringBuilder;(I)Ljava/lang/StringBuildertoStringequals(Ljava/lang/Object;)Z! /*��!"
                                                                   #$   %& <x�Y�Y���L�:6�T�
�
 +�
�.4>EKPq▒���HK,'�!▒!f+,b-1_23[43 X567� 89:;;�V<=        >? u▒L*+��
                    "#&'"@323�;AB0
.J/
```

Dari sini pun sudah jelas flag nya, apalagi kalo dibuka pake VS Code, malah dapet kode aslinya
```java
// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Base64;

public class SafeOpener {
   public SafeOpener() {
   }

   public static void main(String[] args) throws IOException {
      BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
      Base64.Encoder encoder = Base64.getEncoder();
      String encodedkey = "";
      String key = "";

      for(int i = 0; i < 3; ++i) {
         System.out.print("Enter password for the safe: ");
         key = keyboard.readLine();
         encodedkey = encoder.encodeToString(key.getBytes());
         System.out.println(encodedkey);
         boolean isOpen = openSafe(encodedkey);
         if (isOpen) {
            break;
         }

         System.out.println("You have  " + (2 - i) + " attempt(s) left");
      }

   }

   public static boolean openSafe(String password) {
      String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}";
      if (password.equals(encodedkey)) {
         System.out.println("Sesame open");
         return true;
      } else {
         System.out.println("Password is incorrect\n");
         return false;
      }
   }
}
```