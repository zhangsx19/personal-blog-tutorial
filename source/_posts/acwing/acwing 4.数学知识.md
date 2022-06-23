---
title: acwing 4.数学知识
date: 2022-04-14 10:35:24
categories:
- acwing
tags:
- algorithm
toc: true
---
**摘要：acwing算法基础课学习笔记**
<!-- more -->
# 一、数论
## 试除法
### 质数判定
![20220516095643](https://s2.loli.net/2022/05/16/nscD357uBbYtdvk.png)
### 求约数
![20220605195550](https://s2.loli.net/2022/06/05/KTrVuya7qxSvcUb.png)
## 分解质因数
![20220516100331](https://s2.loli.net/2022/05/16/wCDprviqU1f4PoR.png)
```c++
for(int i=2;i<=x/i;i++){
    if(x%i==0){
        res = res/i*(i-1);
        while(x%i==0)x/=i;
    }
}
if(x>1)res = res/x*(x-1);//x是质数
```
## 筛质数
先从小到大把每个数的倍数筛掉，剩下的就是质数
证明：如果p没被筛掉，说明2~p-1均不是p的约数
![20220516102304](https://s2.loli.net/2022/05/16/3GpfxReTUhIzrZ8.png)
优化：埃氏筛法--可以只把质数的倍数筛掉(p可以分解质因数)
![20220516102519](https://s2.loli.net/2022/05/16/TVC5DjUwOtdz3Wy.png)
优化：线性筛法(数量大时快一倍)
![20220516103707](https://s2.loli.net/2022/05/16/7wjuFIbBGDrTE6f.png)
当i枚举到x之前一定会先枚举到x/i，此时会通过st[prime[j]*i]把x=prime[j]*i预先筛掉。
已经找到了最小质因子就可以提前break掉
![20220516103746](https://s2.loli.net/2022/05/16/B4WECaZJ83lySIu.png)

## 最大公约数(辗转相除法)
![20220605204919](https://s2.loli.net/2022/06/05/J2lZSHovKXd9Ici.png)
a和0的最大公约数是a，因为0可以整除任何数

## 欧拉函数
### 筛法求欧拉函数和
![20220605212415](https://s2.loli.net/2022/06/05/RVteIvLJABa2Wjk.png)
### 欧拉定理
![20220605220419](https://s2.loli.net/2022/06/05/zoj6VZgPBdQsi3G.png)
# 二、快速幂
pow(a,b)的时间复杂度是O(b)，即每次乘b，都得再运算一次，快速幂为O(logb)，二进制思想
模板
```c++
int qmi(int m, int k, int p)
{
    int res = 1 % p, t = m;
    while (k)
    {
        if (k&1) res = res * t % p;
        t = t * t % p;
        k >>= 1;
    }
    return res;
}
```
## 快速幂求乘法逆元
![20220605223311](https://s2.loli.net/2022/06/05/MaDn7uW1Eht8SXm.png)
费马小定理
![20220605223341](https://s2.loli.net/2022/06/05/Sx4q8UGsihDkgcz.png)

# 三、扩展欧几里得算法
![20220605224801](https://s2.loli.net/2022/06/05/RQAOvIxlFyYtgW8.png)
![20220606104354](https://s2.loli.net/2022/06/06/SwaG6rFnJzN7iWj.png)
求所有解
![20220606105405](https://s2.loli.net/2022/06/06/OKrCamThW5fU14B.png)
## 线性同余方程
![20220606110507](https://s2.loli.net/2022/06/06/ivbW2j1Te7DKfX6.png)

## 中国剩余定理
![20220606114432](https://s2.loli.net/2022/06/06/VgbEvIRBu9lodUA.png)
用到上一题的不定方程的所有解的形式
![20220606122634](https://s2.loli.net/2022/06/06/LqgNEz5oeUSdWaJ.png)

# 四、高斯消元
![20220606160912](https://s2.loli.net/2022/06/06/2XWsiawyfgKbUx7.png) 

# 五、求组合数
![20220606170423](https://s2.loli.net/2022/06/06/ZON2Kd5Gn9SEW4b.png)
![20220606171251](https://s2.loli.net/2022/06/06/b4LVCEgFmAdqp6M.png)
## 卢卡斯定理
![20220606172842](https://s2.loli.net/2022/06/06/VyHITtm6xhicDLd.png)

![20220606180515](https://s2.loli.net/2022/06/06/s1EBrHxf3edwuSt.png)
## 高精度乘法

# 六、卡特兰数
1.给定 n 个 0 和 n 个 1，它们将按照某种顺序排成长度为 2n 的序列，求它们能排列成的所有序列中，能够满足任意前缀序列中 0 的个数都不少于 1 的个数的序列有多少个。
2.n个数字入栈和出栈的方案数
![20220608103842](https://s2.loli.net/2022/06/08/q2D4KpGW6us8oRZ.png)

# 七、容斥原理
2进制表示：第n位是1表示第n个集合被选，$1到2^n-1$恰好可以表示所有选法,如有5个集合，11100表示|S5∩S4∩S3|

# 八、博弈论
先手必胜：拿完之后剩下的是必败状态，那么我就是必胜状态
先手必败：如果下一步都是必胜状态，那我就是必败状态
公平组合游戏ICG:(如Nim)
1.由两名玩家交替行动
2.在游戏进程的任意时刻，可执行的合法行动与轮到哪名玩家无关
3.不能行动的玩家判负
## Nim
镜像操作
若先手操作所有数异或不是0，一步后一定可以让所有数的异或变成0：
拿走$a_i-(a_i XOR x)$,即拿走后令$a_i$变成$a_i XOR x$
![20220608120308](https://s2.loli.net/2022/06/08/Tw94C2WGLe3yunm.png)

## 有向图游戏
给定一个有向无环图，图中有一个唯一的起点，在起点上放有一枚棋子。两名玩家交替地把这枚棋子沿有向边进行移动，每次可以移动一步，无法移动者判负。该游戏被称为有向图游戏。
任何一个公平组合游戏都可以转化为有向图游戏。具体方法是，把每个局面看成图中的一个节点，并且从每个局面向沿着合法行动能够到达的下一个局面连有向边。

（以当前局面作为图中的一个节点，由当前局面可以到达的局面作为当前节点的后继节点，那么整体就可以形成一个图的结构，这样的一个公平组合游戏就形成了一个“有向图游戏”。）
## Mex运算
设S表示一个非负整数集合。定义mex(S)为求出不属于集合S的最小非负整数的运算，即：
mex(S) = min{x}, x属于自然数，且x不属于S
## SG函数 -解决博弈论的利器
![20220608123436](https://s2.loli.net/2022/06/08/57EtI2UGTKHALki.png)
玩家每次可以选择任何一个图
![20220608135948](https://s2.loli.net/2022/06/08/v2BUoPRfp3AL75u.png)
![20220608135907](https://s2.loli.net/2022/06/08/TmdwWljV6u4CO7R.png)

## 台阶nim
![20220608160053](https://s2.loli.net/2022/06/08/TJlPqjeMHLY12uw.png)
先手必胜策略：让对手看到的永远是1,3级台阶石子个数相等，直至0,0

## 拆分Nim
SG函数
SG定理：SG(a,b)=SG(a)^SG(b),即多个局面的SG值等于各个局面SG值的异或


---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)