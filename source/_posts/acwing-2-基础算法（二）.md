---
title: acwing 2.基础算法（二）
date: 2022-04-14 23:26:47
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
# 一、高精度
## 1.高精度加法
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
## 2、高精度减法
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
## 3、高精度乘法
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
## 4、高精度除法
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
# 二、前缀和数组
## 1.一维
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
## 2.二维
![20220415121504](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220415121504.png)
---

# 参考资料
1.[acwing算法基础课](https://www.acwing.com/)