---
title: acwing 1.基础算法
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
---
# 零、如何学
```
主要思想 <-- 上课
理解并背过代码模板 <--快速默写并调试通过
题目 <--提高熟练度(写完删掉重写一遍，重复3-5遍)
```
# 一、基础算法（一）
## 排序
### 快速排序 --基于分治
```
确定分界点x：q(l),q(r),q((l+r)/2),随机
调整区间：保证左边的数<=x,右边>=x
递归处理左右两边
```
难点是如何调整区间
```
#暴力做法
开两个数组a[],b[]
遍历q[l~r],若<=x,插到a;若>x，插到b
a[]->q[],b[]->q[]
```
```
#优美做法(双指针)
创建两个指针L,R(也可用序号表示)
L一直向右移，直到找到一个>x的数，停下
R一直向左移，直到找到一个<=x的数，停下
#此时L指向的数应放到右边，R指向的数应放到左边
swap L，R对应的数，此时L指向的就是<=x的，R指向的是>=x的
重复直至L,R相遇
```
![502e472c029fc8232a9555c8b26f942](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs502e472c029fc8232a9555c8b26f942.jpg)

怎么判断递归的序号起止？
```
j停留的位置一定不满足>x,即q[j]<=x
i停留的位置一定不满足<x,即q[i]>=x
sort(q,l,j)   //sort(q,l,i-1)
sort(q,j+1,r) //sort(q,i,r)
```
注意边界问题：
```
若递归选择i，则分界点不能是q[l];j同理不能是q[r]
中间点q[(l+r+1)/2]是万能的,建议选中点，也不容易超时
如样例：n=2,q=[1,2]
第一次递归时i=j=0,sort(q,0,-1),sort(q,0,1);
会无限循环sort(q,0,1)
```
快排模板如下：
```
void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i ++ ; while (q[i] < x);
        do j -- ; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}
```
注意：分界点不一定=x
#### 变形：第k个数
![20220419055456](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220419055456.png)

k每次更新成新区间第k小的数，所以每次新区间要重新编号

时间复杂度O(2n)
### 归并排序 --分治
快排是先排后递归，归并是先递归再排
```
确定分界点：mid = (l+r)/2
递归排序left,right
把两个有序的数组合成一个(难点)  <--双指针 (合并链表也是同样的原理)
```
![20220414152022](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220414152022.png)

如果两个值相同，一般是把第一个序列的指针往后移动一位（归并排序是稳定的）

归并模板如下：
```
void merge_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int mid = l + r >> 1;
    merge_sort(q, l, mid);
    merge_sort(q, mid + 1, r);

    int k = 0, i = l, j = mid + 1;
    while (i <= mid && j <= r)
        if (q[i] <= q[j]) tmp[k ++ ] = q[i ++ ];
        else tmp[k ++ ] = q[j ++ ];

    while (i <= mid) tmp[k ++ ] = q[i ++ ];
    while (j <= r) tmp[k ++ ] = q[j ++ ];

    for (i = l, j = 0; i <= r; i ++, j ++ ) q[i] = tmp[j];
}
```
## 二分
### 整数二分
只要看到有序序列，一定想到二分，或先排序后二分。每次保证更新的闭区间里一定有答案。

![20220414163319](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220414163319.png)

为什么第一种模板mid有一个+1？

如果mid=(l+r)/2，如果某次划分的二分区间是[l,r]且l=r-1，则mid=下取整(l+r)/2
=l,若check判断为true的话，则更新的区间仍为[l,r],即无限循环
```
mid=l+r>>1
check(mid)
```
模板如下
```
bool check(int x) {/* ... */} // 检查x是否满足某种性质

// 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;    // check()判断mid是否满足性质
        else l = mid + 1;
    }
    return l;
}
// 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
```

二分法一定有解，题目可能无解，无解时，返回值的含义是第一个满足条件的。
### 浮点数二分
保留六位小数
```
r-l>=1e-8 //经验值是保留的位数+2，若不满足要求可进一步提高精度
```
注意浮点数一定是严格按照[l,mid],[mid,r]来分的
因为没有mid+1或mid-1，所以mid=(l+r)/2，不必再考虑+1的问题

浮点数模板如下：
```
bool check(double x) {/* ... */} // 检查x是否满足某种性质

double bsearch_3(double l, double r)
{
    const double eps = 1e-6;   // eps 表示精度，取决于题目对精度的要求
    while (r - l > eps)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;
}
```
# 二、基础算法（二）
## 1.高精度
### (1)高精度加法
四种类型：
```
A+B len(A)<=1e7
A-B 
A*a a<=1e10
A/a
```
大整数的存储：低位在数组左边，高位在数组末尾
原因；加法进位要补位数，在数组末尾补比数组头部补容易(要整个数组往后移动一位)
模板：
```
// C = A + B, A >= 0, B >= 0
vector<int> add(vector<int> &A, vector<int> &B)
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}
```
### (2)高精度减法
![20220415005054](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220415005054.png)

模板：
```
// C = A - B, 满足A >= B, A >= 0, B >= 0
vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```
### (3)高精度乘法
到下一位时，权重少10倍

![20220415004903](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220415004903.png)

模板：
```
// C = A * b, A >= 0, b >= 0
vector<int> mul(vector<int> &A, int b)
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}

```
### (4)高精度除法
![20220415004957](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220415004957.png)

模板：
```
// A / b = C ... r, A >= 0, b > 0
vector<int> div(vector<int> &A, int b, int &r)
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```


## 2、前缀和数组
### (1)一维
定义$S_N = a_1+a_2+...+a_N,S_0=0$,如果已经算出来了S,则[l,r]区间的a数组和为$S_r-S_{l-1}$,时间复杂度为O(1)
模板：
```
const int N =1e6+10;
int a[N],S[N];
int n,m,l,r;
int main(){
    scanf("%d%d",&n,&m);
    for(int i = 1;i<=n;i++)scanf("%d",&a[i]);
    for(int i = 1;i<=n;i++)S[i]=S[i-1]+a[i];
    while(m--){
        scanf("%d%d",&l,&r);
        printf("%d\n",S[r]-S[l-1]);
    }
    return 0;
}
```
### (2)二维
![20220415121504](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220415121504.png)
---

## 3.差分
### (1)一维
差分是前缀的逆运算

![20220418214005](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220418214005.png)

构造：初始化$\{a_n\},\{b_n\}$为0，看做n次插入，每次插入$a_n$,插入时可看做[n,n]区间加上$c = a_n$,所以不需要考虑构造的问题。即先构造$\{b_n\}$,再根据$\{b_n\}$写出$\{a_n\}$

复杂度：每次+c从O(n)-->O(1)

### (2)二维
a[i][j]存放差分数组b[i][j]所有左上角的和

$b_{x1,y1}+=c,则该点所有右下角的a都会+c$

![20220419003428](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220419003428.png)

---
# 总结
这节课学了排序(包括快排、归并)和二分(整数、浮点数)的模板

参考资料：

1.[acwing](https://www.acwing.com/blog/)