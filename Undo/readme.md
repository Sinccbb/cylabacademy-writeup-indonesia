Lihat ini
```shell
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KW9zOHIwMG5uLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: undo
Incorrect. Try again.
Output: [Error] Command not allowed.
Hint: Try reversing: base64

Enter the Linux command to reverse it: base64 -d
Correct!

--- Step 2 ---
Current flag: )os8r00nn-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it: rev
Correct!

--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-nn00r8so)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: tr '-' '_'
Correct!

--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_nn00r8so)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: tr 'A-Za-z' 'N-ZA-Mn-za-m'
Incorrect. Try again.
Output: picoCTF(Revers1ng_t3xt_Tr4nsf0rm@t10ns_aa00e8fb)
Hint: Try reversing: tr '{}' '()'

Enter the Linux command to reverse it: tr '{}' '()'
Incorrect. Try again.
Output: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_nn00r8so)
Hint: Try reversing: tr '{}' '()'

Enter the Linux command to reverse it: tr '{}' '()'
Incorrect. Try again.
Output: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_nn00r8so)
Hint: Try reversing: tr '{}' '()'

Enter the Linux command to reverse it: tr '()' '{}'
Correct!

--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_nn00r8so}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: tr 'A-Za-z' 'N-ZA-Mn-za-m'
Correct!

Congratulations! You've recovered the original flag:
>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_aa00e8fb}
```
ya kurleb gitu dah, aku lagi males nulis write up hari ini TvT 
https://learn.cylabacademy.org/library/766?page=1&category=5&workspace=true
