---
title: acwing 6.贪心
date: 2022-04-14 10:35:24
categories:
- CS
- algorithm
tags:
- algorithm
- acwing
- C++
toc: true
---
**摘要：acwing算法基础课学习笔记**
<!-- more -->
# 一、区间问题
## 区间选点
![20220513193646](https://s2.loli.net/2022/05/13/phyjrLaV9xoUtzN.png)
只有问题是单峰的才能用贪心，即必须是全局最优解而不是局部最优解
排序：左端点，右端点，双关键字排序
证明：首先，这样取出来的点一定能保证所有区间都有一个点，即为一个合法方案CNT，最优解ANS是所有合法方案的最小，即ANS<=CNT
接下来证明ANS>=CNT即可，只把“否则”内的区间列出来，下一个选择点的区间一定和上一个没有任何交集，由于是按照右端点从小到大枚举，所以下一个区间一定在上一个的右边。现在每两个区间是没有任何交集的，一共找出了有CNT个没有任何交集的区间。现在我们想选点ANS来覆盖这些区间，每选一个点只能覆盖一个区间，所以ANS>=CNT
![20220513194524](https://s2.loli.net/2022/05/13/gMzOUHBW2lF1f6d.png)
## 最大不相交区间数量
![20220513203253](https://s2.loli.net/2022/05/13/eqGzQHnvOkAu5jV.png)
## 区间分组
![20220513204547](https://s2.loli.net/2022/05/13/rKnXI78JtUCmyHR.png)
如果存在这样的组，随便挑一个放进去
证明：
![20220513205114](https://s2.loli.net/2022/05/13/CiUvqEIhOsog9bX.png)
这CNT组一定存在一个公共点Li，所以一定有至少CNT组，即ANS>=CNT
## 区间覆盖
>>给定 N 个闭区间 [ai,bi] 以及一个线段区间 [s,t]，请你选择尽量少的区间，将指定线段区间完全覆盖

![20220513212645](https://s2.loli.net/2022/05/13/8aCOgHu3BRoiXYb.png)
因为cnt的右端更大，如果ans里的某个区间不一样，则一定可以被替换成cnt里的区间
![20220513212738](https://s2.loli.net/2022/05/13/qUyMrXCNQGgJA2P.png)

# 二、Huffman树
## 合并果子
每次可以`随意`合并两堆
huffman_tree:数越小的一定深度越深且可以互为兄弟(越深相加得次数越多)

# 三、排序不等式
短作业优先调度(交换调整法证明)
![20220513220302](https://s2.loli.net/2022/05/13/ufgvAxOZMtKhDEo.png)

# 四、绝对值不等式
![20220513221342](https://s2.loli.net/2022/05/13/F1oAS8eUT9yjLQ4.png)

# 五、推公式
![20220513223306](https://s2.loli.net/2022/05/13/r82DwMOfjzICANB.png)
![20220513223357](https://s2.loli.net/2022/05/13/aKjlCd9ukcMAqgU.png)
因为s[i]<wi+si,w(i+1)+s(i+1)<wi+si,所以交换之后的风险值的最大值一定小于交换前的风险值的最大值

# 六、时间复杂度
![20220513224803](https://s2.loli.net/2022/05/13/H7ImWhMqEYo8cfO.png)