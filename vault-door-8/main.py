expected = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 
            0x97, 0xC0, 0xE4, 0xF0, 0x77, 
            0xA4, 0xD0, 0xC5, 0x77, 0xF4, 
            0x86, 0xD0, 0xA5, 0x45, 0x96, 
            0x27, 0xB5, 0x77, 0xE0, 0xB4, 
            0xC1, 0xA5, 0xF1, 0xC2, 0xD1, 
            0xF0, 0xF1 ]
def switchbits(c,p1,p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = (bit1 << shift) | (bit2 >> shift) | rest
    return result

def rscramble(password):
    a = [i for i in password]
    for b in range(len(a)):
        c = a[b]
        c = switchbits(c,6,7)
        c = switchbits(c,2,5)
        c = switchbits(c,3,4)
        c = switchbits(c,0,1)
        c = switchbits(c,4,7)
        c = switchbits(c,5,6)
        c = switchbits(c,0,3)
        c = switchbits(c,1,2)
        a[b] = c
    return a
cuy = rscramble(expected)
ans = [chr(i) for i in cuy]
ans = ''.join(ans)
print("picoCTF{"+ans+"}")