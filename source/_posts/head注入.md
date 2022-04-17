---
title: head注入
date: 2022-04-13 23:45:10
categories:
- CS
- security
tags:
- sql注入
- security
- splmap
toc: true
---
**摘要：本文介绍了head注入是什么及其背后的原理，以及利用sqlmap工具进行head注入的实践**
<!-- more -->
# 前言
[靶场1](http://injectx1.lab.aqlab.cn/Pass-07/index.php)

---
# 一、head注入
HEAD注入条件是知道用户名密码或登录状态

网络中web访问是以IP数据包形式传输数据，每个数据包由头部（head）和数据体（body）组成，head中有访问者的各种信息。

有的网站他会为了保存我们的信息作为比对会把head头中的信息保存到数据库中以便下一次使用。通讯时我们若能抓到请求数据包，并将头部中身份信息修改则为HEAD注入。抓包实例如下（使用burp）

就像图中User-Agent本意是表示你是哪种访问方式例如苹果、微软、安卓、华为等等，图中我把他的值更换为了一个注入语句，并报错就返回了我关心的结果。

# 二、用到的函数：
```
updataxml或extractvalue #报错函数 head注入是通过引起报错，来返回需要的信息，所以不需要回显点
concat
```
下面详细讲解UPDATEXML (XML_document, XPath_string, new_value);
```
第一个参数：XML_document是String格式，为XML文档对象的名称，文中为Doc
第二个参数：XPath_string (Xpath格式的字符串)<--有特定要求格式
第三个参数：new_value，String格式，替换查找到的符合条件的数据
作用：改变XML_document文档中符合XPATH_string的值
```
注入语句为
```
updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1)
```
其中的concat()函数是将其连成一个字符串，因此不会符合XPATH_string的格式，从而出现格式错误，爆出错误`ERROR 1105 (HY000): XPATH syntax error: '得到的数据'`

---
# 总结


---
# 参考资料
1.[渗透测试基础-HEAD注入](https://blog.csdn.net/weixin_45488495/article/details/115525372)

