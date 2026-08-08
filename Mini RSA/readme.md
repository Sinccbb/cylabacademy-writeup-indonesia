# Write-up: Mini RSA (cylabacademy)

- **Category   :** Cryptography
- **Difficulty :** Medium
- **Author     :** Lim Almadyuni (Limath)
- **Concepts   :** RSA
- **Link       :** [Mini RSA](https://learn.cylabacademy.org/learning-paths/17/139)
---

## Executive Summary
Disini N dan C sangat besar, sehingga hampir mustahil bahkan jika menggunakan factordb.com untuk mencari bilangan prima yang menghasilkan angka besar tersebut (Seolah bisa, tapi pas di klik zonk, itu yang kurasain). Tapi perlu diketahui bahwa $e = 3$, dan perlu diingat pada [Write up Mind your Ps and QS](https://github.com/Sinccbb/cylabacademy-writeup-indonesia/tree/0a764d0bc73729df06437d241be32db6398a8151/Mind%20your%20Ps%20and%20Qs) bahwa $C = M^e mod N$, dan jika $M^e < N$, maka $C = M^e mod N = M^e$, sehingga $C = M^e$, maka $M = \sqrt[e]{C}$
