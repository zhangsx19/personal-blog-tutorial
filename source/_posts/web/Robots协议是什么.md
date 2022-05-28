---
title: Robots协议是什么
date: 2022-04-09 14:58:21
categories:
- CS
- security
tags:
- python
- robots协议
- spider
- url
toc: true
---
**摘要：本文介绍了Robots协议是什么，以及如何利用urllib的robotparser模块，实现网站Robots协议的分析**
<!-- more -->
# 前言
做XCTF时遇到了[Robots协议](https://adworld.xctf.org.cn/task/answer?type=web&number=3&grade=0&id=5063&page=1),特此记录。

---
# 一、前置内容
## 1.区分进程和线程
进程是cpu资源分配的最小单位（是能拥有资源和独立运行的最小单位）

线程是cpu调度的最小单位（线程是建立在进程的基础上的一次程序运行单位，一个进程中可以有多个线程）。单线程与多线程，都是指在一个进程内的单和多。
```
- 进程是一个工厂，工厂有它的独立资源
- 工厂之间相互独立
- 线程是工厂中的工人，多个工人协作完成任务
- 工厂内有一个或多个工人
- 工人之间共享空间
```
```
- 工厂的资源 -> 系统分配的内存（独立的一块内存）
- 工厂之间的相互独立 -> 进程之间相互独立
- 多个工人协作完成任务 -> 多个线程在进程中协作完成任务
- 工厂内有一个或多个工人 -> 一个进程由一个或多个线程组成
- 工人之间共享空间 -> 同一进程下的各个线程之间共享程序的内存空间（包括代码段、数据集、堆等）
```
## 2.浏览器是多进程的
浏览器之所以能够运行，是因为系统给它的进程分配了资源（cpu、内存）

简单点理解，每打开一个Tab页，就相当于创建了一个独立的浏览器进程。如果再多打开一个Tab页，进程正常会+1以上

注意：在这里浏览器应该也有自己的优化机制，有时候打开多个tab页后，可以在Chrome任务管理器中看到，有些进程被合并了 （所以每一个Tab标签对应一个进程并不一定是绝对的）

![20220409151615](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409151615.png)

## 3.浏览器有哪些进程
```
-浏览器主进程：只有一个，主要控制页面的创建、销毁、网络资源管理、下载等。
-浏览器渲染进程(浏览器内核)：每个Tab页对应一个进程，互不影响。
-第三方插件进程：每一种类型的插件对应一个进程，仅当使用该插件时才创建。
-GPU进程：最多一个，用于3D绘制等。
```

## 4.输入网址并解析
这里我们只考虑输入的是一个URL结构字符串，如果是非 URL 结构的字符串，则会用浏览器默认的搜索引擎搜索该字符串。

![20220409152032](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409152032.png)

输入URL后，浏览器会解析出协议、主机、端口、路径等信息，并构造一个HTTP请求。
(两次命中看缓存)
```
-浏览器发送请求前，根据请求头的expires和cache-control判断是否命中（包括是否过期）强缓存策略，如果命中，直接从缓存获取资源，并不会发送请求。如果没有命中，则进入下一步。
-没有命中强缓存规则，浏览器会发送请求，根据请求头的If-Modified-Since和If-None-Match判断是否命中协商缓存，如果命中，直接从缓存获取资源。如果没有命中，则进入下一步。
-如果前两步都没有命中，则直接从服务端获取资源。
```
## 5.HSTS
由于安全隐患，会使用 HSTS 强制客户端使用 HTTPS 访问页面。详见：[你所不知道的 HSTS](https://www.barretlee.com/blog/2015/10/22/hsts-intro/)。
当你的网站均采用 HTTPS，并符合它的安全规范，就可以申请加入 HSTS 列表，之后用户不加 HTTPS 协议再去访问你的网站，浏览器都会定向到 HTTPS。无论匹配到没有，都要开始 DNS 查询工作了。

## 6.DNS域名解析
在发起http请求之前，浏览器首先要做去获得我们想访问网页的IP地址，(如百度的IP是202.108.22.5，在浏览器中输入https://baidu.com和http://202.108.22.5是等价的）浏览器会发送一个UDP的包给DNS域名解析服务器

![20220409153058](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409153058.png)

## 7.备份文件名
常用的备份文件名有.git,.svn,.swp,.~,.bak,.bash_history

# 二、robots协议
Robots协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准（Robots Exclusion Protocol），用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取。它通常是一个叫作robots.txt的文本文件，一般放在网站的根目录下。

当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，如果存在，搜索爬虫会根据其中定义的爬取范围来爬取。如果没有找到这个文件，搜索爬虫便会访问所有没有被口令保护的页面。

如下是一个robots.txt的样例：
```
User-agent: *
Disallow: /
Allow: /public/
```
上面的User-agent描述了搜索爬虫的名称，这里将其设置为*则代表该协议对任何爬取爬虫有效。

Disallow指定了不允许抓取的目录，比如上例子中设置为/则代表不允许抓取所有页面。

# 三、robotparser 
以简书为例，首先创建RobotFileParser对象，然后通过set_url()方法设置了robots.txt的链接。接着利用can_fetch()方法判断了网页是否可以被抓取。
```py
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
```

# 四、解题
## 1.思路1
![20220409154739](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409154739.png)

## 2.思路2
利用[direarch](https://github.com/maurosoria/dirsearch)目录扫描工具暴力破解，扫到有robots.txt
---
# 总结
学习了robots协议和python爬虫的robotparser类。

---
# 参考资料
1. [从输入URL开始建立前端知识体系](https://juejin.cn/post/6935232082482298911)

2. [【Python3网络爬虫开发实战】3.1.4-分析Robots协议](https://juejin.cn/post/6844903576142102535)

3. [从浏览器多进程到JS单线程，JS运行机制最全面的一次梳理](https://juejin.cn/post/6844903553795014663)