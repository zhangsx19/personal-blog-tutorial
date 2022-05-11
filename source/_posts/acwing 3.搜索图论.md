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
# 一、DFS
![20220510112906](https://s2.loli.net/2022/05/10/FkLJG2S7EurPhmD.png)

n皇后：
每行只能放一个皇后，即每行都有一个皇后
![20220510120041](https://s2.loli.net/2022/05/10/WnaiNLbhoGd8rzS.png)
![995172e634b54f450cb5cb48f8004e3](https://s2.loli.net/2022/05/10/PEinxQ4BgTMm6lo.jpg)

# 二、BFS
走迷宫：

![20220510141921](https://s2.loli.net/2022/05/10/wS5pel1EHo2tf4h.png)
# 三、树与图的深度优先遍历
![20220510152158](https://s2.loli.net/2022/05/10/huZagXePAHvLwyT.png)

邻接表存储的次序无关紧要，头插法

树的重心：(无向无环图)，重心连了n个点，删掉重心后，n个点分别形成1个连通块

![20220510154354](https://s2.loli.net/2022/05/10/kB4aOt6qKL7Vbvl.png)

# 四、树与图的广度优先遍历
![20220510162826](https://s2.loli.net/2022/05/10/naFCLKx4VewWtgG.png)

# 五、拓扑排序
有向无环图才有且一定有拓扑序列，所以有向无环图被称为拓扑图
(自环也不行)

准确定义：若一个由图中所有点构成的序列 A 满足：对于图中的每条边 (x,y)，x 在 A 中都出现在 y 之前，则称 A 是该图的一个拓扑序列。

自环：有边(x,x)，但x在A中并不出现在x之前

![20220510163555](https://s2.loli.net/2022/05/10/G1NMLe2zDxsQAHg.png)
![20220510164015](https://s2.loli.net/2022/05/10/qbFNK4yMYWB3aGV.png)

一个有向无环图，一定至少存在一个入度为0的点(反证法)

为什么删掉t到j的边？因为t先入队已经发生了，删不删j都在t后面入队

# 六、Dijkstra
![20220511111522](https://s2.loli.net/2022/05/11/8Ttqu9P3dQvLbIo.png)

## 朴素dijkstra(稠密图)
![20220511112901](https://s2.loli.net/2022/05/11/eoIFz325ajD9LWw.png)

dijkstra:贪心(稠密图用邻接矩阵存，稀疏图用邻接表存)
其余:动态规划

无向图是一种特殊的双向有向图

自环:只需初始化dist[1]=0，可无视。重边:只保留距离最短的那条边

## 堆优化dijkstra(稀疏图)
![20220511120040](https://s2.loli.net/2022/05/11/R7yqMJeTD2vUS9u.png)

# 七、bellman-ford
![20220511141058](https://s2.loli.net/2022/05/11/cenVB3jl4ZY9i8C.png)
第k次迭代：最短路不超过k条边
若第n次迭代有更新：最短路为n条边->n+1个点->有两个点相同->存在负环(更新了)(找负环)
一般前k次迭代d[a]=$\infin$,k+1次才更新
如果限制了最短路经过的边数，有负权回路也无所谓
![20220511144441](https://s2.loli.net/2022/05/11/nSzWI392KPbURq8.png)
更新过程中可能发生串联，解决方法：更新过程中只用上一次的结果(backup数组，memcpy)
![20220511144612](https://s2.loli.net/2022/05/11/2Zafm5Y9yslNpLU.png)
# 八、spfa
## spfa求最短路
要求没有负权回路(一般最短路都没有)
bf算法中只有a变小了b才会变小
![20220511144747](https://s2.loli.net/2022/05/11/2dz79ukEwKyUGnr.png)
![20220511145917](https://s2.loli.net/2022/05/11/z7lh1Wj9vtrbNaQ.png)
queue里存的是每次更新后到起点距离变小的点，入队时要判断一下如果队列已经有b就不用重复入队(但值还是会更新成更小值)
基本思想：我更新过谁才能再拿谁来更新别人，一个点如果没被更新过的话，直接拿它来更新别人一定是没有效果的(重复的)，只有我变小了我后面的才会变小
网格状的最短路通常会被卡成O(nm)
![20220511153628](https://s2.loli.net/2022/05/11/UNY4vBILHh9b17e.png)
## spfa求负环
思路与bf算法一样，都是抽屉原理，证明存在环
经过i->i点后，1到t的总路径变小了，所以是负环，否则环不会存在。(因为存的是最短路径，否则在dist[i]+w时不会更新成有环的路)
此时初始化时不能只入队1,因为有负环的路不一定起点是1，要把所有点都放入队
# 九、Floyd
可以有负边，不能有负环
![20220511181326](https://s2.loli.net/2022/05/11/Di3XTprBOCxHzNU.png)

d[N][N]为邻接矩阵
重边和自环：d[a][b] = min(d[a][b],w);
# 十、prim

# 十一、Kruskal

# 十二、染色法判定二分图

# 十三、匈牙利算法
 
---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)