---
title: windows系统py2和py3的共存与切换
date: 2022-05-25 18:58:50
categories:
- CS
tags:
- python
toc: true
---
**摘要：本文介绍windows系统如何同时安装Python2和Python3，以及如何兼容并切换使用**
<!-- more -->
# 一.安装和配置必要依赖
## 1.下载python2.7.15
[py2](https://link.juejin.cn/?target=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-2715%2F)
![20220525194734](https://s2.loli.net/2022/05/25/7peS1mnxOqaQCZB.png)
## 2.安装python2
不论python2还是python3，python可执行文件都叫python.exe，在cmd下输入python得到的版本号取决于环境变量里哪个版本的python路径更靠前，毕竟windows是按照顺序查找的。
![20220525195039](https://s2.loli.net/2022/05/25/mUqxsR61bBW5u8l.png)

# 二、切换
```
py -2调用python2，py -3调用的是python3.
py -2 -m pip install xxx
py -3 -m pip install xxx
当python脚本需要python2运行时，只需在脚本前加上#! python2，然后运行py xxx.py即可。
同理#! python3
```
原理是python3以后会自动在C盘windows目录安装一个py.exe作为python的版本管理器(读取py.ini和注册表的python路径？所以安装python的路径要想好，之后不能随便移动)



---
# 总结

---
# 参考资料
1.[教你们如何切换Python2与Python3](https://juejin.cn/post/7045530893317832740)