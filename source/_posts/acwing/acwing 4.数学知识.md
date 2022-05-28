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
## 质数判定
![20220516095643](https://s2.loli.net/2022/05/16/nscD357uBbYtdvk.png)
## 分解质因数
![20220516100331](https://s2.loli.net/2022/05/16/wCDprviqU1f4PoR.png)
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
# 二、组合计数

# 三、高斯消元

# 四、简单博弈论


---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)