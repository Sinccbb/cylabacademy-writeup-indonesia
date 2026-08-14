# Write-up: [Irish-Name-Repo 1](https://learn.cylabacademy.org/learning-paths/7/64) (cylabacademy)

- **Category   :** Web Exploitation
- **Difficulty :** Easy
- **Author     :** Chris Hensler
- **Written by :** Lim Almadyuni (Limath)
---

## Executive Summary
Soal ini adalah soal eksploitasi web yang umum, yaitu mengenai SQL Injection, format umum dari SQL injection tuh simpel, seperti ini
```mysql
SELECT * FROM users WHERE username = '$user' AND password = '$password';

```
## Flag
```picoCTF{s0m3_SQL_85832275}```
