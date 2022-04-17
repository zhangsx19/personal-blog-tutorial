---
title: sql注入控制目标服务器
date: 2022-04-17 10:54:51
categories:
- CS
- security
tags:
- trojan
- sql
- 
- 
toc: true
---
**摘要：本文完成了sql注入控制目标服务器的实战项目**
<!-- more -->
# 前言
实战项目：用sql注入控制目标服务器

---
# 一.必备知识
## sql注入
![20220417114033](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417114033.png)

## sql注入与trojan
```
select ··· into outfile ····  #  将查询的内容写入数据库的文件(可新增)
Eg：select 'woaini Eleven' into outfile 'c:/WWW/AAAAA.txt'
```
waf:会过滤and、or、=等关键词,如双写绕WAF`and --> aandnd`

# 二、实战思路
```
1.判断网站的应用方向
电商类：业务逻辑漏洞，主要针对网站一些功能点
门户类：信息泄露出来的漏洞，综合类的
论坛类：站点层的漏洞
2.了解网站技术架构
java、中间件...
3.CMS识别
有的话--> 找漏洞复现
没有的话 --> 黑盒测试（信息收集+漏洞种类）

细节：(burp-repeater快速看response)不改变验证码情况下，网站依然对我们输入的密码做出了判断 --验证码可重复利用漏洞  -->任意用户注册
在任何平台提交漏洞，看的不是种类，而是漏洞危害

信息收集，
		你找到了1个站，你掌握了5个漏洞，你有机会测试5个地方。
        你找到了n个站，你掌握了5个漏洞，你有机会测试n*5个地方。

信息收集 --> 扩大攻击面
漏洞种类 -->  扩大攻击点
```


---
# 总结


---
# 参考资料

