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

## pHp2
![20220516174816](https://s2.loli.net/2022/05/16/cUuTyizS9jZWbrY.png)

注意：这里需要将admin进行二次编码才可成功，因为浏览器会自动进行一次url解码，解码之后传递给代码相当于没进行编码，还是admin

最后，又去看了一下御剑，发现我的字典里没有.phps结尾的，能扫出来就怪了。--御剑的能力取决于字典

```
.phps文件就是php的源代码文件，通常用于提供给用户（访问者）查看php代码，因为用户无法直接通过Web浏览器看到php文件的内容，所以需要用phps文件代替。其实，只要不用php等已经在服务器中注册过的MIME类型为文件即可，但为了国际通用，所以才用了phps文件类型。
它的MIME类型为：text/html, application/x-httpd-php-source, application/x-httpd-php3-source
```