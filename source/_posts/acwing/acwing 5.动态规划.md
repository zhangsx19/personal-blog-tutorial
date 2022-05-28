---
title: acwing 5.动态规划
date: 2022-04-14 10:35:24
categories:
- acwing
tags:
- algorithm
toc: true
---
**摘要：acwing算法基础课学习笔记**
<!-- more -->
# 一、背包问题
## 01背包
$f[i][j]=max(f[i-1][j],f[i-1][j-v[i]]+w[i])$
## 完全背包
朴素做法：比较耗时O(nV^2)
![20220512140820](https://s2.loli.net/2022/05/12/omitc4NMbLjWHGw.png)
优化：O(nV),也可以用滚动数组(j从小到大时f[j-v[i]]实际上是f[i][j-v[i]],因为比较小的j先更新了)
![20220512142726](https://s2.loli.net/2022/05/12/loGLzysBr8meOJ3.png)
## 多重背包
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
朴素方法：和完全背包问题一样，只是k改成了si且k*v[i]<=j
二进制优化：
因max没有减法，不能直接用完全背包的优化
思路：用10个新的物品来表示原来的物品->01背包
![20220512145101](https://s2.loli.net/2022/05/12/hRygDJwn4zFU2Cc.png)
![20220512145215](https://s2.loli.net/2022/05/12/DSzG2HuBUbFq4Ec.png)
复杂度：O(nVlogs)
实现：在输入数据时就直接拆分物品->01背包，注意新的物品总个数N=n*(logs+1)
## 分组背包
每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是 vij，价值是 wij，其中 i 是组号，j 是组内编号。
不能用滚动数组了

# 二、线性dp
如背包问题是二维状态，以i,j为二维坐标，发现状态的更新是一行一行地做的，即线性dp
## 数字三角形
![20220512211553](https://s2.loli.net/2022/05/12/Q2qMDiXsnxHYU7G.png)
注意初始化时的边界问题(j要从0到i+1)
从终点出发会更简单，不用考虑边界问题，最后直接输出f[1][1]
## 最长上升子序列
状态表示几维原则：一定要能让答案表示出来，维数越小越好
![20220512214038](https://s2.loli.net/2022/05/12/kdQ7ipAUJMRYIqL.png)
集合里的区间不一定合法，需满足倒数第二个数a[j]<a[i]。
f[i] = max(f[j] + 1);(j满足0~i-1,且a[j]<a[i])
时间复杂度=状态数*计算每个状态的时间
求方案(子序列是什么)：把转移记录下来
![20220512215319](https://s2.loli.net/2022/05/12/jZ9KX5RzGefYFmd.png)
## 最长公共子序列
一般涉及到两个字符串都可以用(i,j)表示第一个字符串的前i个和第二个字符串的前j个
![20220512222303](https://s2.loli.net/2022/05/12/FQpBNq5fotXCDbL.png)
01∈f[i-1,j]∈f[i,j]，用f[i-1,j]代表01会有重复元素，但求max允许重复的存在，但求子序列数量的话就不行。
因为f[i-1][j-1]∈f[i-1][j]+f[i][j-1]所以通常不写第一项
优化：二分法
![20220513093312](https://s2.loli.net/2022/05/13/Amp7tSMBqrOGdKz.png)

## 最短编辑距离
![20220513101345](https://s2.loli.net/2022/05/13/9bG5rDJlZ4cRiIT.png)


# 三、区间dp
## 石子合并
以最后一次合并的分界线来分类(左边一堆，右边一堆)
![20220512225936](https://s2.loli.net/2022/05/12/XpdGx1EFW6yLPAO.png)
![20220512234533](https://s2.loli.net/2022/05/12/EQvSRgqL74GZmsN.png)
先删除最后一步的合并，再加上。最后一步的合并代价即为i到j的质量总和(可用前缀和s[j]-s[i-1]表达出来)
状态计算时遍历k的值为i到j-1，因为右边至少要有一堆
# 四、计数类dp
属性不再是最值，而是数量
## 整数划分
方法一：完全背包变体
![20220513105933](https://s2.loli.net/2022/05/13/ZPYQzwVWudyBhEr.png)
![20220513112225](https://s2.loli.net/2022/05/13/rc6MDBeUG3yvLE9.png)
容量为0时，前 i-1 个物品全不选也是一种方案，即j恰好等于k*i时，前i-1都不选，只选k个i，也是一种方案
方法二：
每个数需要一直被拆解到1整个过程才能结束
![20220513114813](https://s2.loli.net/2022/05/13/OoAga3KjFmICBQs.png)
# 五、数位统计DP
前缀和思想：
![20220513120832](https://s2.loli.net/2022/05/13/gNdonJYZF5Tylkc.png)
![20220513175115](https://s2.loli.net/2022/05/13/B1Lu5pm7Agv2NFD.png)
对1-9是正确的：
![20220513180557](https://s2.loli.net/2022/05/13/JRQFNB4ahbLoVqG.png)
对0：注意(abc-1)*power(i),因前导0会把0全部去掉
![e07024e4bd5ac043163389245ca14c6](https://s2.loli.net/2022/05/13/aoP4Hzlj9NELcC5.jpg)
# 六、状态压缩DP
## 蒙德里安的梦想
当我们把横向小方格摆好后，竖向小方格就只有一种摆法(即顺次摆1种方案)，所以整个方案数=摆横向小方格的方案数
![20220513152153](https://s2.loli.net/2022/05/13/KROhdUCQnm2NTaS.png)
## 最短哈密顿路径
![20220513160839](https://s2.loli.net/2022/05/13/HCruwkamKyNoPhO.png)
k是所有与j相邻的点
$i=(01110101)_2$表示经过第02456个点,f[i][j]表示从0走到j，经过的所有点是i(也包括0，j),所以f[1][0]=0(表示从点0走到0,经过了点0所以i=1)
# 七、树形DP
![20220513170244](https://s2.loli.net/2022/05/13/WCmAv51RG6pdNfc.png)
![20220513170210](https://s2.loli.net/2022/05/13/RUFZXfWgyAEKx6d.png)
# 八、记忆化搜索
记忆化：每个状态只计算一次，不重复计算
![20220513172237](https://s2.loli.net/2022/05/13/o81wgzm9LQWU2rp.png)
-1表示每个状态还没有计算出来




---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)