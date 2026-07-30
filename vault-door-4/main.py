apaini = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o67 , 0o65 ,
'9' , '6' , '0' , '0' , 'a' , 'b' , 'c' , '3']
ascii_values = [apaini[i] for i in range(8)]
hex_values = [apaini[i] for i in range(8,16)]
gatau = [apaini[i] for i in range(16,24)]
hexa_values = [apaini[i] for i in range(24,32)]
gab = ascii_values + hex_values + gatau
print(gab)
ans = [chr(i) for i in gab]+hexa_values
final_ans = ''.join(ans)
print("picoCTF{" + final_ans + "}")