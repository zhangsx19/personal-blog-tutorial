from audioop import reverse


a2 = [0x5d,0x8b,0x48,1,0x79,0x7d,0xbd,0,0xdd,0x99,0x36,1,0x6b,0x2e,0x3c,0,0xdc,3,0x64,0,0x40,0xa1,0x4c,0,0xdc,0xa5,0x8e,0,0x0a,0x31,0x40,0,0x17,0xc5,0x2f,1,0x53,0x66,0x5c,1,0x33,0xa0,0x92,0,0x67,0x29,0xab,0,0x6c,0x35,0x4c,0,0x2a,0x6c,0x7f,0,0x98,0x8c,0xf4,0,0x2d,0xda,0xf3,0,0x40]

a1 = list("02e0740402e394d402e0606002e01bdc02e07b9c02e0697002e067d402e06b980")
a3 = a1[::-1]
a4050fc = [0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x61,0x62,0x63,0x64,0x65,0x66]
n = len(a1)
print(len(a2))
def fun4():
    v1 = (n>>3)+1
    v3 = {}
    v5 = 0
    for i in range(n):
        v5 |= (ord(a1[i]) - 48)<<8*(i&7)
        if (i&7)==7:
            v3[i>>3] = v5
    v3[i>>3] = v5
    return v3
def fun3():
    v3 = {}
    for i in range(n):
        v3[8*i] = a4050fc[ord(a1[i])>>26&0xf]
        v3[8*i+1] = a4050fc[ord(a1[i])>>22&0xf]
        v3[8*i+2] = a4050fc[ord(a1[i])>>18&0xf]
        v3[8*i+3] = a4050fc[ord(a1[i])>>14&0xf]
        v3[8*i+4] = a4050fc[ord(a1[i])>>10&0xf]
        v3[8*i+5] = a4050fc[ord(a1[i])>>6&0xf]
        v3[8*i+6] = a4050fc[ord(a1[i])>>2&0xf]
        v3[8*i+7] = a4050fc[ord(a1[i])>>30|4*ord(a1[i])&0xc]
def fun2(a4,a5):
    v6 = {}
    for i in range(a5):
        result = i
        for j in range(a4):
            v6[j] = ord(a1[j])
            a1[j] = chr(ord(a1[j])^a2[j])
            a2[j] = a2[j]^ord(a3[j])
            a3[j] = chr(ord(a3[j])^v6[j])
    return result


def fun1():
    for i in range(n):
        v12=ord(a1[i])
        v11=a2[i]
        for j in range(16):
            v4=(v12+ord(a3[i]))^a2[i]
            v12=v11
            v11=v4
        v5=v12
        v6=v11
        v7=0x1a^v5
        a1[i] = 0x64f38^v6
        a2[i] = v7

fun4()
fun3()
fun2(n,0xf)
fun1()
print(a1)
