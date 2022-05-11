---
title: acwing 2.数据结构
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
# 前言
cin和scanf一样快的方法:
ios::sync_with_stdio(false);
# 一、数据结构
## 1.链表
### (1)单链表
```
// head存储链表头，e[]存储节点的值，ne[]存储节点的next指针，idx表示数组的存储当前已经用到了哪个节点
int head, e[N], ne[N], idx;

// 初始化
void init()
{
    head = -1;
    idx = 0;
}

// 在链表头插入一个数a
void insert(int a)
{
    e[idx] = a;
    ne[idx] = head;//上一个head等于的idx,必须是这个顺序
    head = idx ++ ;
}

// 将头结点删除，需要保证头结点存在
void remove()
{
    head = ne[head];
}
```
![20220505154742](https://s2.loli.net/2022/05/05/SIQXshFjdBkVqEZ.png)
![20220505155616](https://s2.loli.net/2022/05/05/4dn6b7eqDoUScIL.png)

无法释放空间，因为用了idx++。算法题绝对不要考虑内存泄漏的问题

单链表可以用O(1)的时间找到下一个点的位置，但是找不到上一个点的位置，只往后看不往前看

### (2)双链表
```
易错点：此时第k个插入的数idx=k+1
别忘记初始化r[0]和l[1],以及main函数里要调用
```

## 2.栈和队列
中缀表达式：
（1）双栈，一个操作数栈，一个运算符栈；
（2）运算符优先级，栈顶运算符，和，即将入栈的运算符的优先级比较：
如果栈顶的运算符优先级低，新运算符直接入栈
如果栈顶的运算符优先级高，先出栈计算，新运算符再入栈

![20220508204904](https://s2.loli.net/2022/05/08/7aQxStKpNTYUMwG.png)

这个方法的时间复杂度为O(n)，因为整个字符串只需要扫描一遍。
运算符有+-*/()~^&都没问题
## 3.单调栈
```
#include<iostream>
using namespace std;
const int N = 1e5+10;
int tt,stk[N];
int main(){
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    for(int i=0;i<n;i++){//每个元素最多只会进栈一次，出栈一次，所以时间复杂度O(n)
        int x;
        cin>>x;
        while(tt&&stk[tt]>=x)tt--;
        if(tt)cout<<stk[tt]<<" ";
        else cout<<-1<<" ";
        stk[++tt]=x;
    }
    return 0;
}
```
## 4.滑动窗口
别忘了做完一遍要重新初始化hh和tt
```
while(hh<=tt&&q[hh]<i-k+1)hh++;//用while比用if好，否则k=1时会出问题
while(hh<=tt&&a[q[tt]]>=a[i])tt--;
```

## 5.KMP
求Next数组

![20220507154335](https://s2.loli.net/2022/05/07/qj8geApmhsr7JcD.png)

## 6.trie
![20220507160658](https://s2.loli.net/2022/05/07/IzJfCpgSimshNlO.png)

字符串仅包含小写英文字母，即每个节点最多只能延伸26条边

son[N][26],cnt[N],n表示每个节点的下标，根节点和NULL都为0

最大异或数：
从高位开始考虑，往和当前数字不同的分支走(只有一个分支除外)

只需枚举$C_n^2$种情况，ai,aj和aj,ai是一样的，所以可以边做边插入,不需要全部插入再做。
注意若输入的数<2^31,总的0和1个数为输入的数的数量*31

## 7.并查集
![20220507194538](https://s2.loli.net/2022/05/07/mwSlfKIzdkMobhn.png)
![20220507194550](https://s2.loli.net/2022/05/07/uhcl5AtrikJMjy9.png)

核心代码：
```
int find(int x){
    if(p[x]!=x)p[x]=find(p[x]);
    return p[x];
}
```

进一步优化(路径压缩)：减少树的高度到只有两层->只搜一遍，把经过的所有节点全部指向根节点(代表元素)(接近O(1))

变体：维护额外数据(如集合大小)
初始si[i]=1,只保证根节点的size是有意义的。
```
注意:
数组名不能用size
先变维护的数组(如si),再变p;或者用a_root和b_root分别存储find(a)和find(b)
```
![20220507201217](https://s2.loli.net/2022/05/07/hzSBgH5KvQO93pM.png)

如果a和b已经在一个集合里了，就不进行操作

食物链：
![20220509090549](https://s2.loli.net/2022/05/09/lrL5CUR17ATXKhv.png)

初始化：每个点都是自己集合的根节点，即距离初始化为0

路径压缩仍可用，每次更新把到父节点的距离相加即可

![20220509113036](https://s2.loli.net/2022/05/09/oEduhZNQ4mn2LcP.png)

## 8.堆
完全二叉树：最后一层节点从左到右依次排布
小根堆：每个点都是以这个点为根的所有点的最小值

![20220508003432](https://s2.loli.net/2022/05/08/O3RJwFU2Kdv4iZY.png)

变体：第k个插入的数，额外维护ph[k]=j(第k个插入的数在堆中的下标是j),hp[j]=k(堆中下标为j的点对应的是第k个插入的数)

注意：输入ph[k]要用idx保存起来，因为交换时ph[k]会改变
难点：交换映射(双射)

![20220508010131](https://s2.loli.net/2022/05/08/MNyKe4wAgF9Emjf.png)

## 9.哈希表
### 拉链法
![20220509121612](https://s2.loli.net/2022/05/09/nfhJDz8roXQcjHY.png)
![20220509121532](https://s2.loli.net/2022/05/09/hlgnM5ojImYu8SQ.png)

注意：取模的数要是质数，而且要离2的整次幂尽可能远

一般只有插入和查询，删除即查找的一种，即在找到的数上打一个标记
### 开放寻址法
开数据大小的2-3倍数组

核心是find(int x),如果x在hash中已存在，则返回其在哈希表中的位置,否则返回其应该存储的位置。注意如果到了数组末尾要循环回到0

memset是按字节赋值的，如memset(h,-1,sizeof h)表示每一个字节的每一位bit都是1,整个就是-1。或者INT_MAX=0x3f3f3f3f

### 字符串哈希(解决字符串的利器)
快速判断两个字符串是否相等

核心思想:用P进制的角度把字符串转换成数字

h[i]=字符串前i个字符的哈希值 h[0]=0

![20220509151921](https://s2.loli.net/2022/05/09/3ieWnfrKRzmEqUv.png)
![20220509154817](https://s2.loli.net/2022/05/09/hL7ZGpuYKxy8XWr.png)

图上应为$h[R]-h[L-1]*P^{R-L+1}$
哈希值是$[0,2^{64}-1]$的数。

注意，字符串的位置从 1 开始编号。

## 10.STL
![20220509161645](https://s2.loli.net/2022/05/09/XOmYzs2DItC9uFx.png)

所有容器都有两函数，时间复杂度为O(1)

申请空间时，系统的处理时间与空间大小无关，与申请次数有关

![20220509162658](https://s2.loli.net/2022/05/09/laZeLXSkBby5PD4.png)

vector的比较操作：字典序比较，从高位比较起

定义小根堆的技巧：

`priority_queue<int,vector<int>,greater<int>> heap`

![20220509164418](https://s2.loli.net/2022/05/09/xXvuY5mHaMgzlEK.png)
```
set//没有重复元素 o(logn)
multimap中的key可以重复，所以multimap中没有重载operator[ ]功能。对于重复的元素，查找的时候也是返回中序遍历的第一个元素
bitset//大矩阵 MLE
```
![20220509170153](https://s2.loli.net/2022/05/09/7KGSHIMRjXOVxPg.png)

---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)