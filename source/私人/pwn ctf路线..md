---
title: 
date: 2022-06-10 16:58:50
categories:
- security
tags:
- pwn
toc: true
---
**摘要：本文总结了自己的pwn学习路线**
<!-- more -->
---
# 零、前言
不要花太长时间在一些奇奇怪怪的技巧上，对之后的学习帮助不大
在真正做出并理解一个 pwn 题前，你可能需要的技能：
1.基本的 Linux 命令
2.能编写基本的 C 语言代码
3.基本的逆向能力：IDA静态分析程序逻辑、寻找漏洞点。
4.调试能力：会用 gdb 或 ida remote debugger 调试 linux 下的程序
在漏洞点附近下断点，通过gdb动态跟踪，查看执行流程、观察内存布局，构造exp链
5.能用 python 编写简单的脚本：编写 exp（漏洞利用脚本）时一般都会用到 pwntools 框架。
6.getshell:分两种情况
(1) 内存程序中有getshell函数[system("/bin/sh")]或指令时，直接调用/劫持。
(2) 存程序中没有getshell函数或指令时， 就要编写shellcode
![20220611011304](https://s2.loli.net/2022/06/11/dT6DYeOkougfmBn.png)
# 一.知识点(pwn+re+crypto)
## 基础入门篇：（3-5天）
CTF中的Pwn题目主要是栈溢出、格式化字符串和堆的利用。栈溢出和格式化字符串相对简单，掌握了一些基础和一些绕过技巧之后，利用的思路还是相对固定的。堆的利用比较复杂，纯粹为了入门可以先把堆这块知识放一放。
[学习过程](https://blog.csdn.net/qq_43935969/article/details/104107872)
### 语言
刷oj
### linux
觉得没啥linux基础的可以先刷刷pwnable.kr
### 汇编
目标：熟悉大多数寄存器，操作码，编写简单的汇编程序
建议看王爽写的那本汇编语言，将书本的实验做一遍，然后再了解一下AT&T和intel两种汇编代码风格有什么不同
[intel汇编 和 AT&T汇编 的区别](https://blog.csdn.net/kennyrose/article/details/7575952)
### 计算机组成与原理
玩pwn，入门是栈溢出，要玩栈溢出，栈的构造要了解吧，函数的调用约定(汇编级别上的，尤其是栈帧这个概念，需要熟记)，函数参数的在栈上的分布要知道吧
读csapp
[C语言函数调用栈(一)(二)](https://www.cnblogs.com/clover-toeic/p/3755401.html)
### 工具使用
[Linux下pwn从入门到放弃](https://paper.seebug.org/481/)
[IDA Pro7.0使用技巧总结](https://xz.aliyun.com/t/4205)
[gdb](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html)
[学习历程](https://blog.csdn.net/gyhgx/article/details/53439417)
### 栈溢出
[手把手教你栈溢出从入门到放弃上下](https://zhuanlan.zhihu.com/p/25892385)
[典型的基于堆栈的缓冲区溢出](https://bbs.pediy.com/thread-216868.htm)
[Windows栈溢出原理](https://www.cnblogs.com/wintrysec/p/10616793.html)
[PWN入门系列（四）：栈终结篇](https://www.anquanke.com/post/id/196095)
[linux栈溢出学习笔记](https://kevien.github.io/2017/08/16/linux%E6%A0%88%E6%BA%A2%E5%87%BA%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
[入坑 CTF-PWN 之 栈溢出入门 ](https://www.jianshu.com/p/d4db898762e6)
[Linux栈溢出入门实战篇 ](https://www.anquanke.com/post/id/169554)
[Linux PWN从入门到熟练 ](https://www.anquanke.com/post/id/164530)
[Linux pwn从入门到熟练（二）](https://www.anquanke.com/post/id/168468)
(练习题 https://github.com/desword/pwn_execrise)
### 堆溢出
[安全客堆讲解](https://www.anquanke.com/post/id/163971#h2-1)
[how2heap总结上下](https://www.anquanke.com/post/id/86808)
[理解glibc malloc](https://blog.csdn.net/maokelong95/article/details/51989081)
[malloc堆管理机制](https://blog.csdn.net/qq_29343201/article/details/59614863)
glibc heap的一些利用.
## 进阶篇：（15-20天）
### rop链(5-10天）
[一步一步学ROP之linux_x86篇|x64篇|gadgets和2free篇](https://www.vuln.cn/6645)
[总结：基本 ROP](https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/basic-rop/)
[PWN入门进阶篇（五）高级ROP](https://www.anquanke.com/post/id/196624)
练习（5-10天）
 （1）[PWN学习总结之基础栈溢出](https://0x48.pw/2016/11/03/0x26/ )
 （2）[PWN学习总结之基础栈溢出2](https://0x48.pw/2016/11/21/0x27/)
### 系统保护机制
[缓冲区溢出保护机制——Linux](https://www.cnblogs.com/clingyu/p/8546619.html)
[Linux (x86) Exploit 开发系列教程之七 绕过 ASLR -- 第二部分](https://blog.csdn.net/wizardforcel/article/details/71057216)
[linux pwn入门学习到放弃](https://pandamac.github.io/2020/05/20/linux-pwn%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0%E5%88%B0%E6%94%BE%E5%BC%83/)
[checksec及其包含的保护机制](http://yunnigu.dropsec.xyz/2016/10/08/checksec%E5%8F%8A%E5%85%B6%E5%8C%85%E5%90%AB%E7%9A%84%E4%BF%9D%E6%8A%A4%E6%9C%BA%E5%88%B6/)
### 格式化字符串漏洞原理（3-5天）
格式化字符串漏洞任意读写
（1）漏洞挖掘基础之格式化字符串 https://www.anquanke.com/post/id/82713
（2）格式化字符串漏洞学习 https://veritas501.space/2017/04/28/%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%BC%8F%E6%B4%9E%E5%AD%A6%E4%B9%A0/
（3） 格式化字符串漏洞利用与分析 https://www.jianshu.com/p/097e211cd9eb
总结：  https://ctf-wiki.github.io/ctf-wiki/pwn/linux/fmtstr/fmtstr_example/**
### elf的文件结构
必读程序员的自我修养

### 整数溢出
### _IO_FILE结构的利用.
### 内存泄漏
[pwn-内存泄漏one_gadget](https://blog.csdn.net/lee_ham/article/details/81941005)
[glibc里的one gadget](https://xz.aliyun.com/t/2720)
### uaf
[解析ctf中的pwn--Fast bin里的UAF](https://www.cnblogs.com/0xJDchen/p/6175651.html)
### PLT和GOT
### 技巧
[CTF-pwn-tips](https://github.com/Naetw/CTF-pwn-tips)
[【学习笔记】CTF PWN选手的养成（一）](https://blog.csdn.net/prettyx/article/details/103173220)
## 高级篇
### webserver

### 虚拟机
程序实现了一套自定义的指令集，并用软件模拟的方式解析指令。
要么找指令实现的漏洞，要么找跑在该指令集下的程序的漏洞。逆向量比较大。
vm escape 虚拟机逃逸
### 其他malloc
tcmalloc、musl libc 中的 malloc
### 异架构：
arm、mips、risc-v... 同一份 C 源代码，在不同架构上的漏洞点和利用方法可能大相径庭。
有时候还会出一些非常冷门的架构，工具都很难找。这时就需要自己动手了。
### C++ 及其它语言
一些高级语言的特性反编译的结果会比较难懂
### Linux kernel pwn
linux .ko 驱动的漏洞挖掘和利用。
### windows pwn
### 物联网
### 内核
内核提权..ctf中常常是写的驱动的问题.
### 魔改的JS引擎
### 浏览器
### symbolic execution 符号化执行

### fuzz



# 二、教程
CSAPP：学习 x86_64 汇编，重点看第 4 章程序的机器级表示。推荐做一下配套课程中的两个 lab：bomb 和 attack，学习简单逆向和栈溢出，基本的 ROP
程序员的自我修养——链接、装载与库：对pwn入门来说必读的书，能让你更清楚的了解很多pwn知识点背后的逻辑，里面的程序的基本执行流程、符号解析、重定向、动态链接都讲的特别详细，对我们了解程序的执行流程有很多的帮助。
ctf竞赛权威指南(pwn篇)：作为入门，这本书的知识点起码够你学大半年了。更加适合pwn手
b站2020暑期Lilac-pwn入门培训:适合想要快速入门开始刷题的师傅们，其实从博客和题目中学习也是一种比较有效的方法
B站XMCVE 2020 CTF Pwn入门课程:这部视频可以说是全b站最为详细的pwn入门视频了，细节抓的很清楚，缺点就是过于详实，可能会让你缺少一份自己的思考，视频时间也过长，需要耐心观看
b站星盟安全团队
b站君莫笑
CTF Wiki
南大操作系统
[台湾Angelboy](https://www.youtube.com/channel/UC_PU5Tk6AkDnhQgl5gARObA)
# 三、刷题
攻防世界:有很多适合新手的题。通过刷攻防世界的新手题能快速了解到pwn的各种类型的题目,然后再仔细分析各种类型的考点。
国外的pwnable.kr:很多题目比较适合新手。从最简单的入门练习到全宇宙最难的关卡，涉及的知识面最全面
https://pwnable.xyz/ （据说是新手向）
hackme.inndy的pwn （中等）
[Hitcon-Training lab1-lab15](https://xz.aliyun.com/t/3902)台湾大佬Angelboy搞的一个pwn练习题集合（从简单到较难，技巧较多）
台湾的pwnable.tw:最接近真实环境的各种PWN的技能点的练习，如果你能通关，你将是PWN界的绝对大佬
浙大的jarvisoj平台
buuctf:有大量比赛题。这个平台还会每月举办月赛
i春秋平台上的题目

# 四、推荐书籍、网站
x86 汇编语言：从实模式到保护模式:介绍了更加贴近底层、跟操作系统相关的汇编，以及一些 x86 CPU、操作系统的工作原理。初学时不需要看。
0day安全软件漏洞分析技术(第二版)
加密与解密:看其中的工具篇和逆向分析技术篇，逆向分析技术篇详细说明了函数调用约定，函数调用栈帧，c++虚函数等东西
使用OllyDbg从零开始Cracking:学习od使用的教程，动手实践上不错，翻译和配套资料在看雪可以搜到。
漏洞战争:很好的书，里面的案例能调的都值得调一下。
glibc内存管理ptmalloc源代码分析:理解Linux堆管理的必读书
黑客攻防技术宝典(系统实战篇)
黑客之道：漏洞发掘的艺术
黑客反汇编解密
# 五、工具
0.kali虚拟机;[pwndocker](https://github.com/skysider/pwndocker)集成了基本工具
![20220611002547](https://s2.loli.net/2022/06/11/hI6TgcfFZLW3Ule.png)
`docker search pwndocker`
objdump和readelf：可以很快的知道elf程序中的关键信息(Ubuntu自带)

1.pwntools,zio:写exp和poc，主要的用途是跟程序进行交互和方便调试.
2.ida:F5
MAC的ida直接吾爱破解，学习二进制吾爱破解账号应该是标配
```c++
1.shift+F12 //查看string信息 (通常可以看到重要的信息 )
2.Alt + T //查找带有目标字符串的函数
3. F5 //查看 C代码 把鼠标放在某句汇编上F5会到这句汇编的代码
4. Ctrl + F //在函数框中 搜索函数
5. 空格键 //流程图与代码 来回切换
6.x //交叉引用 
7.h //转换10进制和16进制 r转换ASCII
8.n //重命名 整理下程序的命名，能理清楚逻辑
9 g //跳转到地址
```
gdb
[插件 peda](https://www.jianshu.com/p/1476f38e3aa3)
checksec ：linux自带的检查文件开启的保护的工具.检查elf程序的安全性和程序的运行平台(一般来说peda里面自带的就够了)
pwndbg: ctf pwn 中最好用的 gdb 插件，这个工具可以帮助你更好的进行动态分析。还支持一些异架构（mips、arm 等）以及 qemu 的调试
```c++
gdb program //直接gdb+文件名开始调试, frequent
gdb program pid //gdb调试正在运行的程序
gdb -args programs 解决程序带命令行参数的情况 或者 run之后再加上参数
quit or q //退出gdb
shell command args //在gdb调试程序带适合执行shell命令
show //用来获取gdb本身设置的信息
info //用来获取被调试应用程序的相关信息
```
ollydbg    动态分析使用，分析程序的流程。
windbg     windows下的动态分析神器，可以调试内核态，谨慎使用。
4.patchelf:一般用来改变 elf 文件的动态链接库和动态链接器。
5.libc rip：当你泄漏了 glibc 中的地址却没有 glibc 动态链接库时，通过符号和地址中的低 24 bit 有可能找到对应的 glibc
6.LibcSearcher：一个 python 库，功能同上。但里面的 libc-database 有点老了，需要更新一下。
7.glibc-all-in-one：主要用它下载含 debug symbol 的 glibc，这样方便查看堆相关的一些信息。
8.ROPgadget、Ropper：找程序中gadget，一般用 ropper，寻找速度似乎比 ROPgadget 快一些
9.libc-database： 可以通过泄露的libc的某个函数地址查出远程系统是用的哪个libc版本
10.one_gadget：查找libc中的onegadget,覆盖跳转地址然后一把梭
11.seccomp-tools：分析 seccomp 沙盒

# 六、比赛
1.ctftime
2.ctfhub
3.buuoj


---
# 参考
1.[SCU-CTF](https://www.scuctf.com/ctfwiki/pwn/#_19)
2.[pwn入门的一些学习资料](https://www.jianshu.com/p/7133863623e6)
3.[pwn入门指南](https://kr0emer.com/2021/07/19/pwn%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97/#%E4%BD%BF%E7%94%A8ida)
4.[PWN入门基础](http://6par.top/2020/07/03/PWN%E5%85%A5%E9%97%A8%E5%9F%BA%E7%A1%80/)
5.[Pwn入坑指南](https://www.cnblogs.com/wintrysec/p/10616856.html#c7hDN6XH)
6.[linux PWN入坑指南](https://github.com/yyanyi213/pwn/blob/master/guide)
7.[Pwn 入门指南](https://www.d0g3.cn/pwn-introduction.html)
8.[pwn入门](https://mambainveins.com/2020/08/18/2020/08/2020-08-18-pwn_study/)
9.[pwn学科](http://blog.leanote.com/post/xp0int/%5B%E5%85%A5%E9%97%A8%5DCTF%E5%AD%A6%E4%B9%A0)
10.[【CTF】PWN：学习资料汇总](https://blog.csdn.net/DRondong/article/details/94500556)