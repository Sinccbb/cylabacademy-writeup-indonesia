        # if (password.length() != 32) {
        #     return false;
        # }
        # char[] buffer = new char[32];
        # int i;
        # for (i=0; i<8; i++) {
        #     buffer[i] = password.charAt(i);
        # }
        # for (; i<16; i++) {
        #     buffer[i] = password.charAt(23-i);
        # }
        # for (; i<32; i+=2) {
        #     buffer[i] = password.charAt(46-i);
        # }
        # for (i=31; i>=17; i-=2) {
        #     buffer[i] = password.charAt(i);
        # }
        # String s = new String(buffer);
        # return s.equals("jU5t_a_sna_3lpm18gb4c_u_4_m2r640");
s = "jU5t_a_sna_3lpm18gb4c_u_4_m2r640"
ans = [''] * 32
for i in range(8):
    ans[i] = s[i]
for i in range(8, 16):
    ans[23 - i] = s[i]
for i in range(16, 32, 2):
    ans[46 - i] = s[i]
for i in range(31, 16, -2):
    ans[i] = s[i]
cans = ''.join(ans)
print(cans)