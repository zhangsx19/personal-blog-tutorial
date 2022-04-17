---
title: http中的cookie
date: 2022-04-09 16:43:21
categories:
- CS
- security
tags:
- cookie
- head response
- http
toc: true
---
**摘要：本文介绍了http中的cookie是什么**
<!-- more -->
# 前言
做XCTF时遇到了[cookie](https://adworld.xctf.org.cn/task/answer?type=web&number=3&grade=0&id=5065&page=1),特此记录。

---
# 一、cookie的定义
Cookie，有时也用其复数形式 Cookies。Cookie是由服务器端生成，发送给User-Agent,浏览器会将Cookie的key/value保存到某个目录下的文本文件内，如网站根目录下的cookie.php,下次请求同一网站时就发送该Cookie给服务器

一句话，`cookie=用户身份`
# 二、cookie的作用
HTTP cookie就是服务器端发送给浏览器端的一小部分数据，浏览器接收到这个数据之后，可以存起来自己用，也可以在后续发送到server端进行一些数据的校验。

Cookie诞生的最初目的是为了存储web中的状态信息，以方便服务器端使用。比如判断用户是否是第一次访问网站。

又如通过在cookies中存储一些有用的数据，可以将无状态的HTTP协议变成有状态的session连接，或者用来保存登录的权限，下次不用密码即可登陆，非常有用。
一般来说，cookies用在三个方面：
```
- session的管理，用来保存登录状态，从而让HTTP请求可以带上状态信息。
- 用户自定义的设置，这些用户特殊的字段，需要保存在cookies中。
- 跟踪用户的行为信息。
```
在很久很久以前，还没有现代浏览器的时候，客户端的唯一存储就是cookies，所以cookies也作为客户端存储来使用的，但是有了现代的浏览器之后，一般是建议把客户端存储的数据放到其他存储方式中。
为什么呢？
因为每次请求cookies中的数据会自动带上，并且发送到server端，所以如果cookies中存储了太多的数据，就会导致服务器性能的下降。

# 三、cookie注入
当你使用Cookie进行传参的时候 ，传参的值一定要进行URL编码的。
默认浏览器是会URL编码的。  空格--> %20

如果用的数据库是ACCESS，语法比较正规(select后一定要有from即要先找到一个表名)
`b9a2a2b5dffb918c -> md5解码-> welcome`
```
escape() # 函数，作用：进行URL编码
document.cookie = "id=" + escape("171 and 1=2 union select 1,2,3,4,5,6,7,8,9,10 from admin")
```
# 四、解题
![20220409165011](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409165011.png)
![20220409165033](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220409165033.png)
---
# 总结
学习了http中的cookies

---
# 参考资料
1. [HTTP系列之:HTTP中的cookies](https://juejin.cn/post/7001712204512919559)

2. [好好了解一下Cookie(强烈推荐)](https://blog.csdn.net/zhangquan_zone/article/details/77627899)
