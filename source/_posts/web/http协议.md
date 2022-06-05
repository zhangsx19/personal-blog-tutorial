---
title: 
date: 2022-04-18 16:58:50
categories:
- security
tags:
- burp
toc: true
---
**摘要：本文介绍了CSRF漏洞的定义和攻击方法**
<!-- more -->
---
# 一.

# 三、BurpSuite
## 安装和配置
[安装方法](https://bbs.zkaq.cn/t/2404.html)
浏览器代理设置：burp依赖于浏览器代理。安装SwitchyOmega插件。

![20220413143822](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413143822.png)

安装证书：burp默认只能访问http，要访问https的话需要安装CA证书--proxy模块options--import/export CA--export certificate in DER format--导出证书的位置(保存为1.cer)--把证书导入到浏览器里，设置里搜索证书，导入1.cer即可

## 常用模块
### proxy: 抓包
* option可改监听的端口(默认是8080，如果改成8081则浏览器也要改成8081)
* 如果设置Intercept is off，则不会将数据包拦截下来，而是会在HTTP history中记录。
* 注意有时要开启响应拦截才能看到响应信息
### repeater:改包
在需要手工测试HTTP Header中的Cookie或User-Agent等浏览器不
可修改的字段是否存在注入点，以及需要发现复杂的POST数据包中是
否存在SSRF时用到。
Headers标签页既可以方便地添加HTTP头信息，又可以避免在手动
修改HTTP头时因缺少空格等原因产生问题。
Hex标签页更多用于修改HTTP数据包的十六进制编码。比如，可以
将其用在文件上传类型的CTF题目中以截断后缀，或者是使用这些编码
来对WAF进行模糊测试，并让我们可以顺利上传Webshell

### intruder：爆破和Fuzz
#### Target标签页
可以设置攻击目标的地址（Host）和目标端口（Port），并且可以选择是否使用HTTPS
#### Position标签页
四种攻击类型，例如有两个要爆破的变量
Sniper型：只需要设置一个Payload set，在两个变量的位置逐一替换
Payload，每次只替换一个位置，先替换前面再替换后面
![20220528151928](https://s2.loli.net/2022/05/28/IEOMymZACwrbtei.png)
Battering ram型：只需要设置一个Payload set，在两个变量的位置同时替换相同的Payload。
![20220528152001](https://s2.loli.net/2022/05/28/pTJestNBk5PGv2n.png)
Pitchfork型：需要设置两个Payload set，这时候两个变量的位置和两个
Payload set是一一对应的关系。这个类型可以用来进行撞库攻击等，
用你已知的账号密码去测试其他网站。
![20220528152045](https://s2.loli.net/2022/05/28/knqfcldvQMAIT6o.png)
Cluster bomb型
![20220528152101](https://s2.loli.net/2022/05/28/BF9eh2DPdKnYvNz.png)
#### Payload标签页
Payload set可切换每个位置使用的Payload集合
```
Runtime file：用于从文件中加载Payload
Numbers：用于设置数字的开始和结束以及步长
Dates：用于设置日期及日期格式。
Character blocks：用于设置长度爆破，Fuzz超长的Post变量，有时候可以绕过WAF等
custom iterator:https://www.cnblogs.com/007NBqaq/p/13220297.html    
```
#### Options标签页
设置线程、网络连接失败时的重传次数、每次重传前的暂停时间、数据包发送速度、开始时间
为了方便观察结果，一般会将响应信息按照请求的返回长度或响
应状态码进行排序，或者在过滤器中设置匹配字符串或者正则表达
式，以便对结果进行筛选和匹配。

### Comparer：比较
在某些诸如Bool盲注的正确和错误的回显题目中，有时候两次数
据包之间的差别很小，比较难发现，这时可以使用比较模块来进行比
较，以发现差异
![20220528153043](https://s2.loli.net/2022/05/28/EqvKlydwArZX3t8.png)

### project
这里可以将域名（也可以是不存在的域名）与IP进行绑定

### extender：安装插件
CO2:与sqlmap结合，需配置sqlmap位置和jPython
burpFaKeip:可以伪造ip和随机ip爆破

---


