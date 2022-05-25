---
title: web ctf路线
date: 2022-04-18 16:58:50
categories:
- CS
- security
tags:
- web ctf
toc: true
---
**摘要：本文介绍了我学习web的路线**
<!-- more -->
# 一.初期
刚入了web安全的坑，面对诸多漏洞必然是迷茫的，首要任务就是打好网站开发的基础，曾有伟人说过-"自己不会做网站，何谈去找网站的漏洞"，在学习漏洞前，要了解基本网站架构、基础网站开发原理，基础的前后端知识，能够让你之后的漏洞学习畅通无阻。

## html+css+js（2-3天）
前端三要素 html、css、js是被浏览器解析的代码，是构成静态页面的基础。
* 重点了解html和js
* 能力要求：能够写出简单表单，能够通过js获取DOM元素，控制DOM树即可。
* 资料：acwing web课 
* 解题：js审计、xss、csrf

## apache+php （4-5天）
ctf里大部分代码审计都是php,php黑魔法也是常考的
通过apache+phpstudy体会一下网站后端的工作，客户端浏览器通过请求apache服务器上的php脚本，php执行后生成的html页面返回给浏览器进行解析。
* 能力要求：了解基本网站原理，了解php基本语法，开发简单动态页面
* 资料：[菜鸟教程](https://www.runoob.com/);[w3school](https://www.w3school.com.cn/);CTFHub
* 解题：php审计 文件上传

## mysql（2-3天）
之前已经安装的phpstudy可以轻易的安装mysql。大部分网站都会带有数据库进行数据存储
* 能力要求： 能够用sql语句实现增删改查，并且能用php+mysql开发一个增删改查的管理系统（如学生管理系统）
* 资料：[菜鸟教程](https://www.runoob.com/);[w3school](https://www.w3school.com.cn/)
* 解题：SQL注入
## python (2-3天)
* 学习语法、正则、文件、网络、多线程等常用库。
  重点学习requests、BeautifulSoup、re这三个库
* 能力要求： 了解python基础语法，能够用python爬取网站上的信息（requests+BeautifulSoup+re）
* 资料:[菜鸟教程](https://www.runoob.com/);[w3school](https://www.w3school.com.cn/) acwing django课

## 工具
### burp(1-2天)
* 重点学习Proxy、Repeater、Intruder三个模块，分别用于抓包放包、重放包、爆破
* 能力要求： 能够用burpsuite抓包改包、爆破用户名密码。只需初步使用即可，在中期的漏洞学习中去逐渐熟练它
* 资料：https://www.bilibili.com/video/BV1aq4y1X7oE
[30天](https://bbs.pediy.com/thread-261931.htm)

# 中期
此时我们应该对网站已经不再陌生，能够自己动手完成一个简单站点。但我们写出来的代码真的安全吗？进入中期，我们便要开始着眼经典漏洞的学习。

一个漏洞的学习，要搞明白三点（每学完一个漏洞就问三个问题）
```
如何利用这个漏洞？
为什么会产生这个漏洞？
如何修复这个漏洞？
```
## SQL注入（7-8天）
从这里开始被灌输 “永远不信任用户的输入” 的口号。现在sql注入也依旧存在，并且它还在不断衍生出如nosql注入、ORM注入等。
* 能力要求： 能够手工注入出任意表的数据，熟悉三种盲注的手法，能够通过sql注入实现任意文件读取和任意文件写入，能够自己编写一个不含sql注入的查询功能
* 资料：[sqli-labs](https://github.com/Audi-1/sqli-labs) 如何使用它网上有很多教学，wp也有很多大佬写了 [这里贴一个](https://blog.csdn.net/wang_624/article/details/101913584)
[wiki](https://www.scuctf.com/ctfwiki/web/)刷题,看总结
[极客大挑战 2019]EasySQL
[极客大挑战 2019]LoveSQL
[SUCTF 2019]EasySQL

## 文件上传（7-8天）
webshell是可以进行代码执行的木马
文件上传其实就是想办法把webshell上传到目标的服务器上去并成功解析，达到控制目标服务器的目的
* 能力要求： 会写php的webshell，明白webshell的原理，熟悉常见的文件上传绕过方法（如过后缀检测、过文件头检测、过MIME类型检测），能够自己编写一个不含漏洞的上传功能(自己测试)
* 推荐学习资料
[upload-labs](https://github.com/c0ny1/upload-labs) 几乎涵盖所有上传漏洞类型
[wiki](https://www.scuctf.com/ctfwiki/web/)刷题,看总结
* 趁手的webshell管理工具： 蚁剑

## 其他漏洞（14-15天）
以上两个漏洞是初学者最应该掌握也是最典型的漏洞，涵盖了代码执行、文件操作、数据库操作等web应用的主体内容。然而web安全的世界还有很多的漏洞需要你去探索，不过学会了这两种漏洞的你去学其他漏洞定然是游刃有余
```
1.命令执行（RCE）
php常见的代码执行（eval）、命令执行（system）函数
2.文件包含
file协议、php伪协议的利用
3.XSS
通过XSS获取用户cookie
4.CSRF
通过csrf让用户点击恶意链接就触发敏感操作
```
* 资料：[wiki](https://www.scuctf.com/ctfwiki/web/)刷题,看总结

# 后期
## 多多参与CTF赛事
即使是初学者也能够找到一些适合自己能力的赛事，比如极客大挑战、UNCTF、各个大学的新生赛等等都是不错的选择，在比赛中去发现自己知识的不足，然后去针对的补充这部分知识，是很好的学习循环，无需迷茫的去到处获取知识，而是在需要时去学习。
Tips: 或许有人觉得直接刷题是一样的，但完全不是，当下比赛中的题往往更加前沿和流行，你可以找到当下的ctf题目趋势，紧跟技术热点，而且可以多多融入ctf竞技的氛围中，成长的更快。
* [ctfhub](https://www.ctfhub.com/#/index) 可以很方便的查看最近举行的ctf赛事
* [ctftime](https://ctftime.org/)

## 多多看其他师傅的博客
打完ctf比赛的你肯定是想看writeup（答案）的，一般来说赛后过几天就会有很多师傅发出他的writeup，从比赛群、百度等途径都可以找到。多多看看其他师傅的解题思路，关注几个大牛，看看他们发的技术文章，都是很好的学习方法。


---
# 总结

---
# 参考资料
1.[](https://www.cnblogs.com/b1ackc4t/p/15837008.html#%E5%A4%9A%E5%A4%9A%E7%9C%8B%E5%85%B6%E4%BB%96%E5%B8%88%E5%82%85%E7%9A%84%E5%8D%9A%E5%AE%A2)