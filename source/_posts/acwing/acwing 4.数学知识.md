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


# 四、简单博弈论


---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)