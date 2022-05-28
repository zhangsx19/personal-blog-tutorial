---
title: 逆向CTF记录
date: 2022-05-02 18:28:53
categories:
- security
tags:
- reverse
- CTF
toc: true
---
**摘要：本文记录刷过的逆向题**
<!-- more -->
---

# 一、逆向工具
![20220419192055](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220419192055.png)

提前要记住IDA的基操~~
```
1.shift+F12 查看string信息 (通常可以看到重要的信息 )
2.Alt + T 查找带有目标字符串的函数
3. F5 查看 C代码 把鼠标放在某句汇编上F5会到这句汇编的代码
4. Ctrl + F 在函数框中 搜索函数
5. 空格键 流程图与代码 来回切换
6.x 交叉引用 
7.h 转换10进制和16进制 r转换ASCII
8.n 重命名
9 g 跳转到地址
```
[IDA的动态调试(linux)](https://blog.csdn.net/a257131460266666/article/details/124356519)

[IDA的动态调试(gdb)](http://t.zoukankan.com/fply-p-8493504.html)

IDA local windows debugger:直接运行即可，但注意目录不可有中文

对gdb进行强化的两个工具:peda和pwndbg，这两个工具可以强化视觉效果，可以更加清楚的显示堆栈，内存，寄存机的情况。但不兼容，使用时需[切换](https://blog.csdn.net/kevin66654/article/details/86773517)

# 二、怎么看汇编
IDA的start函数是编译器自动生成的，即在main()前要执行一些函数。可通过它找main()函数入口。main有三个参数，argc,argv,envp(环境参数)。如果实在找不到，看汇编
，在IDA提供的入口往下翻，一般main函数call之前会push三个参数

![20220502192136](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502192136.png)
![20220502192715](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502192715.png)

函数、全局变量都是深颜色的，局部变量是浅颜色的

![20220502194640](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502194640.png)
aMwwCTw和input都是字符串，字符串相减，减出来一定是数字才能作为input数组的索引(实在不知道也可以动态调试看地址)
异或肯定是ASCII码或者数字异或，不可能是字符串。取地址*就是取了某一位

LL:long long 看前面的数字即可
# 三、实战题目
## XCTF
### 1.ignite me
拿到exe文件，放到die中脱壳，发现是exe32为程序，所以放到32位的IDA中，
![20220419200241](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220419200241.png)
![20220419200951](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220419200951.png)
![20220420123608](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220420123608.png)

### 2.入门逆向
![20220421121036](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220421121036.png)
这里看到v2和v59这就证明了这是两个数组的运算，所以我们应该将上面的字符串分成两个数组，分别从v2和v59开始
![20220421121102](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220421121102.png)

0x13u的u表示无符号数

### 3.logmein
从伪代码我们可以看到，解密所需要的密钥（v7）应该是字符串，但这里v7是LL型的（长长整形），所以在解密之前需要先将v7还原为字符。

这里转换并不复杂，只需将v7的值转换为hex（16进制）然后再转换为字符串，但由于字符是小端存储，所以转换成字符串后还需对字符串做倒置处理。

### 4.insanity
注意字符串地址(cout有自动识别和转换机制)(&str会编译成&str[0])

![20220501153445](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501153445.png)
![20220501153538](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501153538.png)
![20220501154417](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501154417.png)
![20220501154619](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501154619.png)

发现一个关键的字符串，&strs,发现是取这个字符串输出，然后，跟进strs

### 5.python-trade
步骤：EXE文件转pyc(py2exe:unpy2exe,pyinstall:pyinstxtractor)->检查前8字节是否是`03 f3 0d 0a 76 ed db 57`若不是要补上->pyc转py(uncompyle2)

![20220501155855](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501155855.png)
![20220501162041](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501162041.png)
```
python C:\anaconda3\envs\p2\Scripts\uncompyle2 aaa.pyc>aaa.py
```
ord() expected string of length 1, but int found

在python3下运行会出错而python2不会，原因是因为ord()这个函数接受的类型是一个长度为1的字符串，而在python3当中传入的i已经是一个整型数了，直接用i-16就可以完成操作

### 6.re1
```c
memset()//作用是将某一块内存中的内容全部设置为指定的值
memset(首地址,值,sizeof(地址总大小));
memset(a,0,sizeof(a)) //初始化数组a为0
```
![20220501170656](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501170656.png)

看看哪里涉及v5，可以看到开头的_mm_storeu_si128(），对其进行分析发现它类似于memset(),将xmmword_413E34的值赋值给v5，所以，我们可以得到正确的flag应该在xmmword_413E34中，然后，我们双击413E34进行跟进

![20220501170738](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501170738.png)
![20220501170809](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501170809.png)

这时，我们使用IDA的另一个功能 R ，能够将十六进制的数转换为字符串。(注意小端读取)

解法二：ODB中文搜索ASCII

解法三：ODB调试，发现判断时有个寄存器写入了flag,复制所有寄存器到剪贴板即可

![20220501171020](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501171020.png)

### 7.Hello, CTF
![20220501173913](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501173913.png)
![20220501174104](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501174104.png)

### 8.no-strings-attached
有两种方法可以获得flag，一种是分析decrypt()函数计算flag，另一种是动态调试。

![20220501211833](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501211833.png)

banner就是输出两个字符串，prompt_authentication也是输出个字符串，最后剩下authenticate。

静态分析：显然s和dword都是数组， 每个元素占4字节(地址加4),字符串数组末尾的0要舍去。malloc也把v2的值赋给了dest

![20220501220329](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501220329.png)
![20220501220902](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501220902.png)

提取&s(提取&dword同理)
可参考[IDA Python提取数据](https://blog.csdn.net/XFox_/article/details/120587417)
```py
addr=0x08048AA8   #数组的地址
arr = []
for i in range(39):    #数组的个数
    arr.append(Dword(addr+4* i))
print(arr)
```
解密脚本：
```py
s = [5178, 5174, 5175, 5179, 5248, 5242, 5233, 5240, 5219, 5222, 5235, 5223, 
5218, 5221, 5235, 5216, 5227, 5233, 5240, 5226, 5235, 5232, 5220, 5240, 
5230, 5232, 5232, 5220, 5232, 5220, 5230, 5243, 5238, 5240, 5226, 5235, 5243, 5248]
a2 = [5121, 5122, 5123, 5124, 5125]
v6 = len(s)
v2 = v6
v7 = len(a2)
dest = s
v4 = 0
while(v4<v6):
    for i in range(v7):
        if v4<v6: 
            dest[v4] -= a2[i]
            v4 += 1
        else:
            break
for i in range(len(dest)):
    print(chr(dest[i]),end="")#取消自动换行
```

动态调试：
```bash
gdb no-string-attached
b *0x08048725 #下断点
r #运行
x/6sw $eax #查看eax的值
n #单步运行一行高级语言命令
ni #单步执行一条汇编指令
disass 某个函数 #查看某个函数的汇编代码
x/6sw $eax （使用examine命令（简写是x）来查看内存地址中的值）
x /nfu 地址
n：输出单元的个数
f：显示格式，可以是下面的值(x:16进制
t:二进制
o:八进制
d:10进制
s:字符串)
u：单元长度，可以是下面的值(
b:代表字节
h:代表双字节
w:代表word，通常是4字节
g:代表八字节
)
```
![20220501213505](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501213505.png)

### 9.csaw2013reversing2
在菜单上的“Edit”、“Segments”、“Rebase program...”里将“Value”的值加上TargetApp的ASLR偏移。即Value = 0x400000+偏移量

![20220501233408](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220501233408.png)

注意_debugbreak()会设置断点并进入调试状态，此时若是动态调试的话会因为双重调试器使得程序退出，直接改成nop指令即可(汇编层面是Trap to Debugger)

第二个坑：if里面是没有弹框的，执行完解密就直接退出了！可以修改汇编的jmp到弹框地址

要先看C或C++伪代码再分析反汇编结构图最后才看反汇编文本！！！！
我吃了很多亏在这里，总是以为能直接看懂汇编，但是无法掌握汇编的结构！

静态调试：根据sub_401000的解密算法自己仿照C语言或python脚本解密，因为参数都可以跟踪到

这里是四个字节显示的，又由于小端存储，所以顺序是颠倒的，我们可以将其转换成一个字节(Byte,Word(2 Byte),Dword(4 Byte))查看,地址+1是1个Byte

![20220502005225](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502005225.png)
![20220502010017](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502010017.png)
```py
x=[0xbb,0xaa,0xcc,0xdd]
y=[0xBB,0xCC,0xA0,0xBC,0xDC,0xD1,0xBE,0xB8,0xCD,0xCF,0xBE,0xAE,0xD2,0xC4,0xAB,0x82,0xD2,0xD9,0x93,0xB3,0xD4,0xDE,0x93,0xA9,0xD3,0xCB,0xB8,0x82,0xD3,0xCB,0xBE,0xB9,0x9A,0xD7,0xCC,0xDD]
i=0
z=[]
while i<len(y):
    t=chr(y[i]^x[i%4])
    z.append(t)
    i+=1
print(z)
print(''.join(z))
```
### 10.getit
![20220502183422](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502183422.png)

可以看到先判断v5是否大于s存储字符串的长度，然后通过运算，最后将得到的flag写入文件。
但是有意思的地方在flag.txt文件所在的位置是/tmp目录，这个目录是Linux下的临时文件夹，程序运行完，生成flag的txt文件被清理了，所以我们找不到文件。所以自然地想到动态调试

### 11.迷宫
[参考解答](https://blog.csdn.net/weixin_52865102/article/details/122676013)

![20220502210618](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220502210618.png)

## 12.calcKey.elf
先file查看一下

![20220509212045](https://s2.loli.net/2022/05/09/2OGDpHMh8sEZPSr.png)
```
Stripped和not stripped的最大区别：
stripped：将程序中的符号表的信息剔除掉了，这样子编译出来的可执行文件体积比较小；
not stripped：则反之，但是就是因为其保留了这些信息，所以便于调试。
一般最终的程序都会使用strip来减小可执行文件的体积。而调试中的程序则不使用strip。
```

# 四、遇到的问题
## 1.反编译时positive sp value has been found
栈sp不平衡，在options->General->Disassembly显示栈指针，然后发现提示的语句有负值(显示为负，实际为正，即实际中栈指针ESP不能为正值)，修改上一条语句直至提示的语句的栈指针显示为正值