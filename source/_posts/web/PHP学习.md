---
title: php学习
date: 2022-05-22 18:28:53
categories:
- security
tags:
- PHP
toc: true
---
**摘要：本文记录php学习过程**
<!-- more -->
---
# 前置知识
在浏览器中输入网址到返回页面的过程
输入url回车，会先访问配置好的DNS服务器地址查找域名对应的IP，如果能查到DNS服务器就把要找的IP地址发回来，如果查不到就到根域名服务器。
根域名服务器(很少)记录了哪些服务器是负责查.com，哪些是.xyz等等，再让我们去对应的服务器依次向下询问，问到了就把IP返回浏览器
![20220522204320](https://s2.loli.net/2022/05/22/OvadcpuxICMVo6U.png)
![20220522204059](https://s2.loli.net/2022/05/22/HRfsIX2WEMqCyUk.png)
![20220522204549](https://s2.loli.net/2022/05/22/DAjJBK6OnokVU7Z.png)
Apache服务器只接受IP访问，不接受域名访问，所以需要DNS
```
apache服务器：安装了apache软件的电脑
dns服务器：安装了dns软件的电脑
mysql服务器：安装了mysql的电脑
IIS、nginx
```
![20220522205632](https://s2.loli.net/2022/05/22/HCRxA1tlMqEb84g.png)

# 一、安装环境
win10虚拟机
phpstudy集成了apache,php,mysql,phpmyadmin,zend,[使用教程](https://www.xp.cn/wenda/376.html)
```
WAMP:Windows+apache+mysql+php LAMP则是Linux
端口可省略，默认是80(http)
```
动态页面：内容会定期更新

web服务器是软件(apache,IIS,nginx)每一个网页伺服器程式都需要从网络接受HTTP请求，然后提供HTTP回复给请求者
浏览器只能执行三种前端，无法执行php文件，会无视php内容
静态页面内容是不变的，扩展名是html，这种你浏览器请求的话，不经过服务器处理，服务器就直接传给你了；动态页面的内容是根据条件变化的，可能每个人看到的都不一样，动态页面里的代码是服务器处理过后才传给浏览器的。
那么服务器怎么知道这个文件该不该处理之后再传呢？最简单的办法就是根据扩展名区分，服务器遇见.php的后缀就会先处理再发给浏览器。php页面也可以包括html内容，如果.php文件都是html内容，那么相当于php处理器打开文件看了下，没啥处理的就直接丢给浏览器了。如果请求的是.html，apache默认不会发给php应用服务器

如果本机没有运行环境，php文件是运行不了的。如果把扩展名改成.html或者.htm后，直接点击就可以打开，但是其中`php代码是不会执行和显示的`。
![20220523020037](https://s2.loli.net/2022/05/23/Frln8AfIogYkSGd.png)
php应用服务器(软件)执行php代码并把结果返回apache

# 二、php语法
## 1.基本语法
?>结束标志隐含了一个分号，所以有时最后一行可以不加分号
## 2.变量
使用变量之前是不需要声明的
变量的销毁
```php
unset($变量名称)
$and1=1;
unset($and1);//销毁$and变量
echo $and1;//提示出错，因为变量已经被销毁了！
```
可变变量
```php
$abc='test';//定义了一个变量$abc里面存了值test
$$abc='孙胜利';//$test='孙胜利';
echo $test;
```
引用
```php
$a='test';
$b=$a;//相当于把$a的值，复制一份再赋值给$b这个变量
$b=&$a;//相当于给$a起了一个别名，操作其中任何一个，都会影响到另外一个变量的值!
$b=20;
echo $a;
```
变量类型(弱类型语言)
bool
```php
以下值被认为是false，其他的值都是被认为是true
	①布尔值false
	②0
	③浮点型0.0
	④空白字符串和字符串0//空白字符串指的是直接一对单引号或者双引号里面没有任何内容
	⑤没有成员的数组
	⑥NULL
var_dump输出变量类型 int(100)
```
NULL
null表示一个变量没有值，表示空，如被unset函数销毁的变量
string (字符串)
```php
$b=100;
$a='test$bdwqd\'wqdqw';//test$bdwqd'wqdqw,转义\
$a='te$bst......';//te$bst......
$a="te{$b}st......";//te100st......
echo $a;
//定界符
$b=200;
$a=<<<aaa
字符串内容
aaa;//aaa与变量命名规则类似
```
## 3.常量
定义：define('常量名称',常量值) 或者 define("常量名称",常量值)
defined()函数来检查是否定义了某个常量
常量一旦被定义就不能被重新定义或者取消定义
********常量可以不用理会变量范围的规则而在任何地方定义和使用(预定义常量)

## 4.预定义常量
PHP内核已经帮我们定义好了的常量
其中有的预定义常量是以__开头的，这些预定义常量我们又叫它魔术常量(代码所在的位置不同他的值也是不同的，所以它叫[魔术常量](https://www.php.net/manual/zh/language.constants.magic.php))
预定义常量是不区分大小写的！

## 5.运算符
字符串运算符
```php
. 连接运算符
$a='孙胜利';
$b='测试字符串连接符';
$c = $a.$b;
echo $c;
echo '<br />';
echo "{$a}{$b}";
```
赋值运算符
$a=$b=2;相当于$a=($b=2);也相当于$a=2;$b=2;
比较运算符
PHP中规定：使用echo输出布尔类型值的时候
```php
echo true;它在页面中会输出1
echo false;它会在页面中什么都不输出
```
在测试的过程中如果需要输出布尔类型值的时候我们最好使用var_dump()来输出更明了的结果
<>和!=是一样的如`$a!=$b即$a<>$b`
逻辑运算符
```php
and 或者 &&
xor
!//逻辑非 如!$a
表达式1 ? 表达式2 : 表达式3;
$a=false ? 10 : 20;//20 $a=false整个表达式值是false
//赋值运算符整个语句是有值的，所以整个语句就是一个表达式，只要是值就是表达式
//如echo $a=$b=2;//2
`可以把系统的命令放在里面执行！`
$a=`ipconfig`;//string(1412) 
$b=`ifconfig`;
var_dump($b);//windows系统无输出
```
![20220523113031](https://s2.loli.net/2022/05/23/USgWke8l1pLia5t.png)
屏蔽表达式@
```php
屏蔽表达式可能发生错误！
$b = 1;
unset($b);
var_dump(@$b);//NULL
```
## 6.流程控制
if、switch、while、for、exit()、die()、

## 7.函数
```php
function 函数名([形式参数1,形式参数2,....形式参数n]){
	//各种PHP代码....
	//......
	return 表达式;//也可以不返回，如果不写那么默认返回null
}
```
参数传递
* 形参
* 引用传参
* 可变长度参数列表：调用时比形参多是允许的
```php
func_get_args();
func_get_arg();
func_num_args();
```
![20220523121026](https://s2.loli.net/2022/05/23/KNnZslFGC4Oz3US.png)
* 可变函数(变量函数)
```php
function test(){
    echo "test";
}
$a = 'test';
$a();//等价于test();
```
## 8.数组
数组创建
```
	方法一、
		变量名称[索引值]=数据;
		变量名称[]=数据;//不写索引值默认是 索引数组，从0开始
	方法二、
		变量名称=array(
			索引值=>数据,
			..........
		);
```
多维数组：
```php
$students = array(
	0=>array(1,'sun',true,60.5),
	1=>array(2,'li',false,20),
	2=>array(3,'han',true,90)
)
```
数组的遍历
for循环(用的比较少，因为有缺陷)
```php
$arr=array(
	'name'=>'sun',
	'age'=>10
)
```
foreach:
```php
foreach(数组变量 as 变量1){
	//每次循环执行的语句
	变量1代表当前正在经历（访问）的数据
}
foreach($arr as $value){
	echo $value;
}
		
foreach(数组变量 as 变量1=>变量2){
	//每次循环执行的语句
	变量1代表当前正在经历（访问）的数据的索引值
	变量2代表当前正在经历（访问）的数据
}
foreach($arr as $key=>$value){
	echo $key.'<br/>';
}
```
预定义超全局数组变量
已经定义好了（存在）的变量(存放的数据的类型是数组)
传递数据（提交数据）给服务器端主要两种方式
```php
	1.get方式
		比如：
		?参数名=参数值&参数名=参数值......
		http://localhost/demo5_3/index.php?参数名=参数值
		在服务器端（请求的php文件这边）可以通过$_GET来获取到
		$_GET索引值为参数名，索引值对应的数据就是参数值
	2.post方式
		比如表单 post发送过来的！
		可以通过$_POST来获取到!
	3.$_REQUEST 既可以接收 get 请求数据,也可以接收 post 请求
```
## 9.字符串处理
去除空格或其他字符函数
```php
1.trim//去除左右两边
		$str='    abc   ';
		var_dump($str);
		var_dump(trim($str));


		$str='abcabcdefac';
		var_dump($str);
		var_dump(trim($str,'bac'));//如果要去除多个字符可以连着写！
2.ltrim
3.rtrim
```
大小写转换函数
```php
strtoupper($str);
strtolower($str);
```
字符串查找函数
```php
1.substr_count
		$str='testteste';
		var_dump(substr_count($str,'te'));//3

		$text2 = 'gcdgcdgcd';
		echo substr_count($text2, 'gcdgcd');//1

		$str='testteste';
		var_dump(substr_count($str,'te',1,8));//不能超出字符串
2.strpos
		$str='testteste';
		var_dump(strpos($str, 't1'));
		if(strpos($str, 't')===false){
			echo '没找到！';
		}else{
			echo '找到啦!';
		}

		$str='testteste';
		var_dump(strpos($str, 't',1));//从str[1]开始找，直到str[3]，返回3
3.strstr
		$str='testteste';
		var_dump($str);
		var_dump(strstr($str,'s'));
		var_dump(strstr($str,'s',true));
```
字符串替换函数
```php
str_replace
$str=array(
		'abc123abc',
		'123abcabc',
		'abcab123c'
	);
var_dump($str);
$str1=str_replace(array('1','2','3'),array('一','二','三'),$str,$count);
echo $count;//count = 9;有九个字符被替换了
var_dump($str1);
```
字符串截取函数
```php
$str='testdqwdwqdwqdqdwq';
echo substr($str,3,2);
```
字符串分隔函数
```php
1.explode
		$str='test,test1,test2,test3';
		var_dump(explode(',',$str,2));//从第一个,分成两部分
2.str_split
		$str='test';
		var_dump(str_split($str,1));//分割后的每部分只含1个字符
```
## 10.正则表达式
正则表达式就是普通字符和特殊字符组成的一个字符串
描述了一类字符串的特征，然后通过这个特征可以配合一些特定的函数，来完成对字符串更加复杂的一系列操作！ 
定界符
	/a/,/表示正则表达式的开始与结束
	还有#a# !a! |a|等
普通字符
元字符
```php
	\d	匹配任意一个十进制数字，等价于[0-9]
	\D	匹配任意一个除十进制数字以外字符,等价于[^0-9]
	\s	匹配任意一个空白字符,比如换页符、换行符、回车符、制表符、垂直制表符
	\S	匹配除空白字符以外的任何一个字符
	\w	匹配任意一个数字或字母或下划线
	\W	匹配除数字、字母、下划线以外的任意一个字符
	.	匹配除换行符以外的任意一个字符
	
	*	匹配0次或1次或多次其前面的字符
	+	匹配1次或多次其前面的字符
	?	匹配0次或1次其前面的字符
	{n}	表示其前面字符恰好出现n次
	{n,}	表示其前面字符出现不少于n次
	{n,m}	表示其前面的字符至少出现n次，最多出现m次
	
	^或\A	匹配字符串开始位置
	$或者\Z	匹配字符串的结束位置
	
	|	匹配两个或多个模式
	
	[]	匹配方括号中的任意一个字符
	[^]	匹配除方括号中字符以外的任意一个字符
	
	()	将括号中作为一个整体以便将其中的内容获取到
		在我们的正则表达式中 可以使用圆括号来将某一段括起来，在圆括号的后面部分，我们可以使用
		\\数字 来代表圆括号部分所匹配到的内容！
```
模式修正符
	常见模式修正符
	i	在和模式进行匹配时不区分大小写
	m	多行匹配，如果目标字符串 中没有"\n"字符, 或者模式中没有出现^或$, 设置这个修饰符不产生任何影响
	s	如果设定了此修正符，那么.将匹配所有的字符包括换行符
	U	禁止贪婪匹配
函数：
```php
preg_match
preg_match_all($p,$s,$arr[])//给定正则表达式，在给定的字符串中搜索，符合特征的部分就提取出来
```	
## 11.文件与目录操作
```php
一、判断普通文件和目录
	1.is_file()//判断给定文件名是否为一个正常的文件
	2.is_dir()//判断给定文件名是否是一个目录
二、文件的属性
	1.file_exists()//检查文件或目录是否存在
	2.filesize()//取得普通文件大小
	3.is_readable()//判断给定文件名是否可读
	4.is_writable()//判断给定的文件名是否可写
	5.filectime()//获取文件的创建时间
	6.filemtime()//获取文件的修改时间
	7.fileatime()//取得文件的上次访问时间
	8.stat()//获取文件大部分属性值
三、目录的基本操作
	1.basename()//返回路径中的文件名部分
	2.dirname()//返回路径中的目录部分
	3.pathinfo()//返回文件路径的信息
	4.opendir()//打开目录句柄
	5.readdir()//从目录句柄中读取条目,返回目录中下一个文件的文件名
	6.rewinddir()//倒回目录句柄
	7.closedir()//关闭目录句柄
	8.mkdir()//新建目录
	9.rmdir()//删除指定的空目录
	10.scandir()//列出指定路径中的文件和目录
四、文件的基本操作
	1.fopen()//打开文件或者 URL
	2.fread()//读取文件
	3.fgets()//从文件指针中读取一行
	4.feof()//测试文件指针是否到了文件结束的位置
	5.fwrite()//写入文件
	6.rewind()//倒回文件指针的位置
	7.flock()//轻便的咨询文件锁定
	8.ftruncate()//将文件截断到给定的长度
	9.fclose()//关闭一个已打开的文件指针
	10.file() //把整个文件读入一个数组中
	11.copy()//拷贝文件
	12.unlink()//删除文件
	13.file_get_contents()//将整个文件读入一个字符串
	14.file_put_contents()//将字符串写入文件中
	15.rename()//重命名一个文件或目录
	16.readfile()//读入一个文件并写入到输出缓冲
五、文件的上传
	文件的上传的过程这些细节我们是不需要管的，都是自动的，上传的文件默认是放在一个临时的目录里面的，我们要做的就是把这些临时目录
	里面的文件移动到我们需要的地方就OK啦！
六、文件的下载
	获取文件的MIME类型
	http://localhost/demo10_4/index.php
	就相当于
	localhost/demo10_4/a.rar
```	
## 12.会话控制
php脚本可以向客户端电脑中设置Cookie：`setcookie ();`
在服务器端上超全局地读取Cookie的内容`$_COOKIE`
删除Cookie:`setcookie("member",'',time()-1);`
![20220523223910](https://s2.loli.net/2022/05/23/rUBxhZuaQWwTI2p.png)
uniqid(random)
session
```php
session_start();
		1)开启一个会话
			一个客户 到超市里面买东西 办会员卡！
			
		2)打开已经存在的会话
			当这个客户 以后再到超市买东西的时候 根据上次办的卡号 买东西！
			根据客户端传来的session id 把这个 session id 对应的数据 读取到 $_SESSION这个变量里面
```	
	
# 三、bbs开发
## 1.需求分析
能够让浏览我们网站的用户可以看其他用户发的帖子，注册成为我们网站的会员之后，还可以回复帖子
父版块：比较大的分类
	子版块：在父版块内再分类
	版主：就是某个子版块的版主,具有删除本分类下面的帖子、回复的权限

## 2.前台和后台界面(html,css,js)

## 3.数据库设计
phpmyadmin创建数据库->整理utf8
父板块信息：id(索引：primary),module_name,sort
文件结构：
```
admin/:存放后台程序文件
inc/:存放被包含的文件(比如自己定义的函数库)
static/:存放样式、图片
uploads:存放上传文件
```
### php与数据库交互(端口是3306)
![20220524193808](https://s2.loli.net/2022/05/24/FnPDUj8zGyhL6Yi.png)
在mysql中，可通过关键字auto_increment为列设置自增属性，只有整型列才能设置此属性，每个表只能定义一个auto_increment列，并且必须在该列上定义主键约束（primary key）(一张表只能有一个主键，用来和其他表互动的)
如果输入的数据库语句中有引号等，必须转义后再执行

### 父板块展示与删除
![20220524203234](https://s2.loli.net/2022/05/24/W75k6ptCNdneMD8.png)
其实就是循环输出html语句

### 操作确认
发现传过去confirm.php的url会有双问号，方法是urlencode

### 编写系统引导程序
迁移到不同服务器：
1.建立好程序需要使用的数据库以及表,以及对应的数据
2.修改config.inc.php配置文件