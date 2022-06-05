---
title: acwing linux
date: 2022-04-14 10:35:24
categories:
- acwing
tags:
- linux
toc: true
---
**摘要：acwing linux课学习笔记**
<!-- more -->
# 一、常用文件管理命令
linux学的是把后端的框架、数据库搭好后，前端就可以调用后端的函数了
```c++
string f(string url){return "html";}
```
## 1.terminal是什么
两个屏幕(命令行)共用一个主机
多个电脑又可以连到一个或多个服务器，服务器一般不会关机
acterminal其实是acwing服务器的终端，可以连接到其他服务器
一般工作时不会用自己的电脑，而是用服务器提供的接口来操作服务器，只要有一个终端就可以了
命令行的好处:有很多批量化操作
## 2.文件系统
```
根目录：/
bin:常用的可执行文件的命令
etc:配置,如部署网站里面会有apache、nginx等的配置文件
var:里面有个log文件夹存日志
lib:保存一些安装包和头文件
home:所有用户的家目录(工作目录)的集合 有用户1，用户2...文件夹
proc:进程相关的信息(计算机的信息，如cat /proc/cpuinfo)
root:根用户的目录
当前用户：~(登录后的默认目录)
```
![20220517224536](https://s2.loli.net/2022/05/17/zqxRfrHBjYyeCbo.png)
## 3.路径
```
绝对路径:从根目录开始描述
相对路径：从当前目录开始描述 tmp/main.cpp(开头无/)
.. ：上层目录
. ：当前目录
访问家目录的tmp文件夹: cd ~/tmp
```
## 4.常用命令介绍
```
(1) ctrl c: 取消命令，并且换行
(2)clear
(3) tab键：如果补全不了快速按两下tab键，可以显示备选选项
(4) ls: list，蓝色的是文件夹，白色的是普通文件，绿色的是可执行文件
ls -l:显示文件长信息(包括权限)
d表示文件夹 -表示普通文件 x是可执行
ls -h 人性化输出
ls -a 输出all隐藏文件(以.开头的文件)
参数位置可以随便变 如ls -ah 和 ls -ha是一样的
(5)cd 默认家目录 cd - 返回上一个待过的目录(只能一个)
(6) pwd: 显示当前路径
(7) cp XXX YYY: 将XXX文件复制成YYY，XXX和YYY可以是一个路径，比如../dir_c/a.txt，表示上层目录下的dir_c文件夹下的文件a.txt(也可以重命名)
复制+粘贴+重命名
(8) mkdir XXX: 创建目录XXX
创建a里有b，b里有c；mkdir a/b/c -p
(9) rm XXX: 删除普通文件;  rm XXX -r: 删除文件夹(递归) rm * ：删除所有
名字有空格用转义字符即可y\ c
支持正则表达式：rm *.txt
(10) mv XXX YYY: 将XXX文件移动到YYY，和cp命令一样，XXX和YYY可以是一个路径或文件；重命名也是用这个命令
剪切+粘贴+重命名
(11) touch XXX: 创建一个文件
(12) cat XXX: 展示文件XXX中的内容
(13) 复制文本
    windows/Linux下：Ctrl + insert，Mac下：command + c
(14) 粘贴文本
    windows/Linux下：Shift + insert，Mac下：command + v
(15)man 和-h同样作用
```
![20220517233344](https://s2.loli.net/2022/05/17/d2YzO93oTXkrNns.png)

# 二、编辑环境：tmux和vim
## 1.tmux
功能：
    (1) 分屏。
    (2) 允许断开Terminal连接后，继续运行进程。
结构：
    一个tmux可以包含多个session，一个session可以包含多个window，一个window可以包含多个pane。

top：任务管理器
![20220518002832](https://s2.loli.net/2022/05/18/K5FdVyovGf2xAZ1.png)
```
(1) tmux：新建一个session，其中包含一个window，window中包含一个pane，pane里打开了一个shell对话框。
(2) 按下Ctrl + a后手指松开，然后按%：将当前pane左右平分成两个pane。
(3) 按下Ctrl + a后手指松开，然后按"（注意是双引号"）：将当前pane上下平分成两个pane。
(4) Ctrl + d：关闭当前pane；如果当前window的所有pane均已关闭，则自动关闭window；如果当前session的所有window均已关闭，则自动关闭session。
(9) 按下ctrl + a后手指松开，然后按z：将当前pane全屏/取消全屏。
(10) 按下ctrl + a后手指松开，然后按d：挂起当前session。
(11) tmux a：打开之前挂起的session。 attach
(12) 按下ctrl + a后手指松开，然后按s：选择其它session。
        方向键 —— 上：选择上一项 session/window/pane
        方向键 —— 下：选择下一项 session/window/pane
        方向键 —— 右：展开当前项 session/window
        方向键 —— 左：闭合当前项 session/window
(18) tmux中复制/粘贴文本的通用方式：
        (1) 按下Ctrl + a后松开手指，然后按[
        (2) 用鼠标选中文本，被选中的文本会被自动复制到tmux的剪贴板
        (3) 按下Ctrl + a后松开手指，然后按]，会将剪贴板中的内容粘贴到光标处
```
## 2.vim
在tmux里vim支持鼠标(注意大小写)
```
G:跳转行(gg是跳转头，G跳转最后行)
\d+空格:跳转该行的第几个字符
d:删除(剪切)模式(dd删除整行)
u:撤销(ctrl+r取消撤销)
y:复制(yy复制整行)
p:粘贴
=:格式化
>:向右缩进
<:向左缩进
```
```
/查找内容+回车 n查找下一个 N查找上一个
:set nonu(无num，即无行号)
:noh(无highlight)
:行号,行号(或1,$)s/w1/w2/g
:行号,行号s/w1/w2/gc 每次询问
```
# 三.shell语言
Linux中常见的shell脚本有很多种，常见的有：
```
Bourne Shell(/usr/bin/sh或/bin/sh)
Bourne Again Shell(/bin/bash)
C Shell(/usr/bin/csh)
K Shell(/usr/bin/ksh)
zsh
```
Linux系统中一般默认使用bash，所以接下来讲解bash中的语法。
文件开头需要写#! /bin/bash，指明bash为脚本解释器。
```bash
chmod +x test.sh  # 使脚本具有可执行权限
bash test.sh # 用解释器执行 不需要 x权限
```
## 1.变量
一般定义的变量都是字符串,=两边不能有空格
```bash
name1='yxc'  # 单引号定义字符串
name2="yxc"  # 双引号定义字符串
name3=yxc    # 也可以不加引号，同样表示字符串
```
使用变量，需要加上$符号，或者${}符号。花括号是可选的，主要为了帮助解释器识别变量边界。
```bash
echo $name  # 输出yxc
echo ${name}  # 输出yxc
echo ${name}acwing  # 输出yxcacwing
echo ${name1}${name2}  # 输出yxcacwing
```
使用readonly或者declare可以将变量变为只读。
```bash
readonly name
declare -r name  # 两种写法均可
```
unset可以删除变量。
```bash
name=yxc
unset name
echo $name  # 输出空行
```
进程与环境变量
bash开一个子进程
![20220518114457](https://s2.loli.net/2022/05/18/GQqEmFYc2fNBLdW.png)
```
自定义变量（局部变量）：子进程不能访问的变量
环境变量（全局变量）：子进程可以访问的变量
自定义变量改成环境变量：export name  # 第一种方法 declare -x name  # 第二种方法
环境变量改为自定义变量：export name=yxc  # 定义环境变量 declare +x name  # 改为自定义变量
```
单引号中的内容会原样输出，不会执行、不会取变量；
不加引号和双引号中的内容可以执行、可以取变量；
```bash
echo 'hello, $name \"hh\"'  # 单引号字符串，输出 hello, $name \"hh\"
echo "hello, $name \"hh\""  # 双引号字符串，输出 hello, yxc "hh"
```
获取字符串长度
```bash
echo ${#name}  # 输出3
name="hello, yxc"
echo ${name:0:5}  # 提取从0开始的5个字符
```
## 2.默认变量
在执行shell脚本时，可以向脚本传递参数。$1是第一个参数，$2是第二个参数，以此类推。特殊的，$0是文件名（包含路径）。例如：
```bash
#! /bin/bash
echo "文件名："$0
echo "第一个参数："$1
echo "第二个参数："$2
echo "第十个参数："${10}
```
然后执行该脚本：
```bash
acs@9e0ebfcd82d7:~$ chmod +x test.sh 
acs@9e0ebfcd82d7:~$ ./test.sh 1 2 3 4
```
文件名：./test.sh
第一个参数：1
第二个参数：2
```bash
$#	代表文件传入的参数个数，如上例中值为4
$*	由所有参数构成的用空格隔开的字符串，如上例中值为"$1 $2 $3 $4"
$@	每个参数分别用双引号括起来的字符串，如上例中值为"$1" "$2" "$3" "$4"
$$	脚本当前运行的进程ID
$(command)	返回command这条命令的stdout（可嵌套） echo $(ls)
```
## 3.数组
定义：数组用小括号表示，元素之间用空格隔开。例如：
array=(1 abc "def" yxc)
也可以直接定义数组中某个元素的值：
```bash
array[0]=1
array[1]=abc
array[2]="def"
array[1000]=yxc
```
读取数组中某个元素的值
```bash
${array[index]}
${#array[*]}  # 数组长度，类似于字符串
```
## 4.expr
expr命令用于求表达式的值,`expr 表达式`
```
用空格隔开每一项
对包含空格和其他特殊字符的字符串要用双引号括起来
expr会在stdout中输出结果。如果为逻辑关系表达式，则结果为真，stdout为1，否则为0。
expr的exit code：如果为逻辑关系表达式，则结果为真，exit code为0，否则为1。
```
字符串表达式
```bash
str="Hello World!"
echo `expr length "$str"`  # `command`或$(command)表示执行该命令，输出12
echo `expr index "$str" aWd`  # 输出7，下标从1开始,0表示不存在
echo `expr substr "$str" 2 3`  # 输出 ell 3为length
```
整数表达式
() 可以该表优先级，但需要用反斜杠转义，也可以将特殊字符用引号引起来
逻辑关系表达式

## 5.read命令(std::cin)
raed name
```
-p: 后面可以接提示信息
-t：后面跟秒数，定义输入字符的等待时间，超过等待时间后会自动忽略此命令
```
## 6.echo(std::cout)
echo -e "hello\nworld"

### printf(跟c++完全一样，只是换成了空格)
printf "%10d.\n" 123  # 占10位，右对齐
printf "%-10.2f.\n" 123.123321  # 占10位，保留2位小数，左对齐
printf "My name is %s\n" "yxc"  # 格式化输出字符串
printf "%d * %d = %d\n"  2 3 `expr 2 \* 3` # 表达式的值作为参数

## 7.test
||和&&是bash自带的
test命令用exit code返回结果，而不是使用stdout。0表示真，非0表示假。
```bash
test 2 -lt 3  # 为真，返回值为0
echo $?  # 输出上个命令的返回值，输出0
```
```bash
二者具有短路原则：可用其实现if else 
expr1 && expr2：当expr1为假时，直接忽略expr2
expr1 || expr2：当expr1为真时，直接忽略expr2
test -e test.sh && echo "exist" || echo "Not exist"
test -e test2.sh && echo "exist" || echo "Not exist"
```
文件类型判断
```bash
test -e filename  # 判断文件是否存在
-f	是否为文件
-d	是否为目录
```
文件权限判断
```bash
test -r filename  # 判断文件是否可读
-w	文件是否可写
-x	文件是否可执行
-s	是否为非空文件
```
整数间的比较
```bash
test $a -eq $b  # a是否等于b
-ne	a是否不等于b
-gt	a是否大于b
-lt	a是否小于b
-ge	a是否大于等于b
-le	a是否小于等于b
```
字符串比较
```bash
test -z STRING	判断STRING是否为空，如果为空，则返回true
test -n STRING	判断STRING是否非空，如果非空，则返回true（-n可以省略）
test str1 == str2	判断str1是否等于str2
test str1 != str2	判断str1是否不等于str2
```
## 8.文件判断
```
-a FILE 如果文件存在则为真。
-b FILE 如果文件是块状的，则为真。
-c FILE 如果文件是特殊字符，则为真。
-d FILE 如果文件是一个目录，则为真。
-e FILE 如果文件存在则为真。
-f FILE 如果文件存在并且是一个普通文件，则为真。
-g FILE 如果文件是set-group-id，则为真。
-h FILE 如果文件是一个符号链接，则为真。
-L FILE 如果文件是一个符号链接，则为真。
-k FILE 如果文件的 “粘性 “位被设置，则为真。
-p FILE 如果文件是一个命名的管道，则为真。
-r FILE 如果文件可以被你读取，则为真。
-s FILE 如果文件存在并且不是空的，则为真。
-S FILE 如果文件是一个套接字，则为真。
-t FD 如果FD在一个终端上打开，则为真。
-u FILE 如果文件是设置了用户身份的，则为真。
-w FILE 如果文件可以被你写入，则为真。
-x FILE 如果文件可由你执行，则为真。
-O FILE 如果文件由你有效拥有，则为真。
-G FILE 如果该文件由你的小组有效拥有，则为真。
-N FILE 如果文件在上次被读取后被修改，则为真。
```
## 9.函数
在函数内，$1表示第一个输入参数，$2表示第二个输入参数，依此类推。
注意：函数内的$0仍然是文件名，而不是函数名。
```bash
func() {  # 递归计算 $1 + ($1 - 1) + ($1 - 2) + ... + 0
    word=""
    while [ "${word}" != 'y' ] && [ "${word}" != 'n' ]
    do
        read -p "要进入func($1)函数吗？请输入y/n：" word
    done

    if [ "$word" == 'n' ]
    then
        echo 0
        return 0
    fi  

    if [ $1 -le 0 ] 
    then
        echo 0
        return 0
    fi  

    sum=$(func $(expr $1 - 1))
    echo $(expr $sum + $1)
}

echo $(func 10)
```
## 10.文件重定向(读写)
read < inputfile
echo > outputfile
```bash
#! /bin/bash
inputfile=$1
outputfile=$2
read n < $inputfile
sum=0
for ((i=1;i<=n;i++))
do
    sq=$(expr $i \* $i)
    sum=$(expr $sum + $sq)
done
echo $sum > $outputfile
```
## 11.引用外部脚本
source test.sh

# 四、ssh
远程登录服务器
```bash
ssh user@hostip
logout #退出
```
第一次登录时会提示：(注意是为了防止登录到一些有害的服务器)
```
The authenticity of host '123.57.47.211 (123.57.47.211)' can't be established.
ECDSA key fingerprint is SHA256:iy237yysfCe013/l+kpDGfEG9xxHxm0dnxnAbJTPpG8.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
输入yes，然后回车即可。这样会将该服务器的信息记录在~/.ssh/known_hosts文件中。(信息泄露)
然后输入密码即可登录到远程服务器中。
ssh的默认登录端口号为22。如果想登录某一特定端口，加入-p 端口号
## 1.配置文件
创建文件 ~/.ssh/config。
```
Host myserver1
    HostName IP地址或域名
    User 用户名

Host myserver2
    HostName IP地址或域名
    User 用户名
```
之后再使用服务器时，可以直接使用别名myserver1、myserver2。不用user@ip了
## 2.密钥登录
创建密钥：`ssh-keygen`然后一直回车即可。
执行结束后，~/.ssh/目录下会多两个文件：
```
id_rsa：私钥
id_rsa.pub：公钥
```
之后想免密码登录哪个服务器，就将公钥传给哪个服务器即可。
例如，想免密登录myserver服务器。则将公钥中的内容，复制到myserver中的~/.ssh/authorized_keys文件里即可。
也可以使用如下命令一键添加公钥：`ssh-copy-id myserver`
![20220518225107](https://s2.loli.net/2022/05/18/Z69U7wHvGhVAB45.png)
## 3.批量化处理多台服务器
ssh user@hostname command
![20220518225818](https://s2.loli.net/2022/05/18/owQdzIgim2rFVT5.png)
```
# 单引号中的$i可以求值
ssh myserver 'for ((i = 0; i < 10; i ++ )) do echo $i; done'
```
## 4.scp
```bash
scp source1 source2 destination # source和destination可以是本地和服务器
scp -r ~/tmp myserver:/home/acs/ #注意-r的位置
scp -P 22 source1 source2 destination #注意大P的位置
使用scp配置其他服务器的vim和tmux
scp ~/.vimrc ~/.tmux.conf myserver:
```
# 五.git
![20220519104746](https://s2.loli.net/2022/05/19/W9iJ7SkqmGbsz8U.png)
```bash
git config --global user.name xxx：设置全局用户名，信息记录在~/.gitconfig文件中
git init --initial-branch=main
git add #添加到暂存区
git commit #添加到版本库的一个版本
git diff XX #查看XX文件相对于暂存区(若暂存区是空，则是HEAD)修改了哪些内容
git restore readme.txt #将工作区的文件恢复到暂存区的状态，若暂存区是空，则恢复到HEAD的状态
git restore --staged readme.txt #把文件从暂存区删除，staged即为暂存区
git log #查看版本从起点到HEAD的路线 
git reflog #查看HEAD指针的移动历史（包括被回滚的版本）  
git reset --hard HEAD^ 或 git reset --hard HEAD~：将代码库回滚到上一个版本，但并不会删除新版本
git reset --hard HEAD^^：往上回滚两次，以此类推
git reset --hard HEAD~100：往上回滚100个版本
git reset --hard 版本号：回滚到某一特定版本
若想回到新版本，可用版本号git reset,版本号即哈希值的前七位(可通过gitref来找HEAD走过的节点)
git remote add origin git@git.acwing.com:zhangsx/linux.git #用户名@服务器ip 
git push -u origin 分支名 #默认都是master分支
```
![20220519110900](https://s2.loli.net/2022/05/19/qCieGa4oVFjKk2r.png)
git是通过ssh和scp来访问和传文件的
SSH 公钥，通常包含在文件 '~/.ssh/id_ed25519.pub' 或 '~/.ssh/id_rsa.pub' 中，并以“ssh-ed25519”或“ssh-rsa”开头
## 多分支
多人开发一般不会在主分支开发，所有分支共用一个暂存区
```bash
git checkout -b branch_name #创建并切换到branch_name这个分支
git branch #查看所有分支和当前所处分支
git checkout branch_name #切换到branch_name这个分支
git merge branch_name #将分支branch_name合并到当前分支上,实质是指针改变了,branch1没删除
git branch -d branch_name #删除本地仓库的branch_name分支
git push -u branch1 #要把分支也push上去
git push -d branch1 #删除云端分支
git pull origin branch_name #将远程仓库的branch_name分支与本地仓库的当前分支合并
```
两个分支都修改了readme.txt

## git stash栈
```bash
git stash #将工作区和暂存区中尚未提交的修改存入栈中
git stash apply #将栈顶存储的修改恢复到当前分支，但不删除栈顶元素
git stash drop #删除栈顶存储的修改
git stash pop #将栈顶存储的修改恢复到当前分支，同时删除栈顶元素
git stash list #查看栈中所有元素
```
# 六、apache thrift(remote procedure call)
## 设计原型
解耦合的微服务框架，不同服务既可以在同一个服务器，也可以在不同服务器上。thrift提供通信服务(类似socket)，即服务器调用另外一台服务器的进程
![20220522134018](https://s2.loli.net/2022/05/22/Q7zl6Vu8dfn2RHj.png)
创建thrift文件夹存储所有thrift提供的接口

## match_client
生成的py文件有个Match-remote可执行文件是用于服务端的，但我们只需要实现客户端，所以直接删掉
![20220522151402](https://s2.loli.net/2022/05/22/gi6yN1dVmEsnOBX.png)
先启动服务端，再客户端：
```py
transport.open() #连接到服务端，开始传输
transport.close() #关闭连接
```

## match_server
```bash
thrift -r --gen cpp match.thrift
#文件结构
|-- gen-cpp
|   |-- Match.cpp
|   |-- Match.h
|   |-- Match_server.skeleton.cpp
|   |-- match_types.cpp
|   |-- match_types.h
|-- match.thrift
|-- save.thrift
```
```bash
g++ -c main.cpp match_server/*.cpp #头文件不用编译，会自动引用
g++ *.o -o main -lthrift #需要用到thrift的动态链接库
g++ *.o -o main -lthrift -pthread #用到了thread库
```
git时最好不要把.o,.swp和二进制文件加进去
```bash
git restore --stage *.o *.swp main
```
### 线程与锁
服务端除了有一个线程去增减用户，还要有一个线程不断匹配用户，所以需要并行
一个玩家匹配的时间越久，匹配的范围应该越大
生产者-消费者模型：消费者不停消耗任务(死循环)
生产者就是add_user和remove_user
生产者和消费者之间的通信媒介：如消费队列(锁mutex)
```c++
mutex m;
p(m)//p操作表示争取这个锁，一旦争取到的话就可以行动
v(m)//其他进程被阻塞
```
比如不能同时读写head
条件变量(condition_variable)对锁进行了封装
```c++
struct MessageQueue
{
    queue<Task> q;
    mutex m;
    condition_variable cv;
}message_queue;
```
线程可能同时执行，即恰好同时存到了队列的同一个head，就会覆盖掉一个本应存的任务，加锁保证同一时间只能有一个线程在操作head
用锁来操作队列：如两个线程同时执行，一个add拿了锁,一个remove会卡死在unique_lock直到拿锁的线程执行完解锁
```c++
int32_t add_user(const User& user, const std::string& info) {
    // Your implementation goes here
    printf("add_user\n");
    unique_lock<mutex> lck(message_queue.m);//无需显式解锁，局部变量注销即解锁
    message_queue.q.push((user,"add"));
    return 0;
  }
```
```c++
 while(true){
    unique_lock<mutex> lck(message_queue.m);//循环完一次会解锁再获得锁
    if(message_queue.q.empty()){
        //防止一直获得锁从而把进程占满
        message_queue.cv.wait(lck);//解锁并卡在这，直至唤醒
        //cv.notify_all();//通知所有wait的条件变量
    }
    else{
        message_queue.pop();
        lck.unlock();
    }
 }
```
刚开始时队列大概率是空，就获得锁，执行完就解锁，就会死循环，所以如果是空是就把这个进程按住，直到非空

### 多线程服务器
```c++
TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);//单线程处理输入输出
//对应client.py里的一次transport.open()和transport.close()
//如果想每调用一次就开一个线程，用多线程服务器，还要定义工厂
```
### 长时间匹配可降低匹配标准
需记录当前玩家等待的秒数=>每次执行match后还在users中的玩家等待秒数+1=>只在队列为空时匹配
![20220604002222](https://s2.loli.net/2022/06/04/sXtV2ZEqGr8cDP9.png)
两重循环匹配(注意a要能匹配b，b也要能匹配a，因为两者匹配标准不一定相同)

# 七、管道
将一个命令执行完后的标准输出作为下一个命令的标准输入
把标准输入看做一个文件
```bash
find . -name *.py | cat #会把标准输入这个文件的内容原封不动地输出
find . -name *.py | xargs cat #xargs会把标准输入转化成文件参数给cat
find . -name *.py | xargs cat | wc -l #wc会把标准输入作为一个文件，并统计该文件
```
# 八、环境变量
列出当前环境下的所有环境变量：
```bash
env  # 显示当前用户的变量
set  # 显示当前shell的变量，包括当前用户的变量;
export  # 显示当前导出成用户变量的shell变量
```
```
常见环境变量
HOME：用户的家目录。
PATH：可执行文件（命令）的存储路径。路径与路径之间用:分隔。当某个可执行文件同时出现在多个路径中时，会选择从左到右数第一个路径中的执行。下列所有存储路径的环境变量，均采用从左到右的优先顺序。
LD_LIBRARY_PATH：用于指定动态链接库(.so文件)的路径，其内容是以冒号分隔的路径列表。预先编译好的，不用再编译
C_INCLUDE_PATH：C语言的头文件路径，内容是以冒号分隔的路径列表。
CPLUS_INCLUDE_PATH：CPP的头文件路径，内容是以冒号分隔的路径列表。
PYTHONPATH：Python导入包的路径，内容是以冒号分隔的路径列表。从左往右的第一个
JAVA_HOME：jdk的安装目录。
CLASSPATH：存放Java导入类的路径，内容是以冒号分隔的路径列表。
```
为何将修改命令放到~/.bashrc，就可以确保修改会影响未来所有的环境呢？

每次启动bash，都会先执行~/.bashrc。
每次ssh登陆远程服务器，都会启动一个bash命令行给我们。
每次tmux新开一个pane，都会启动一个bash命令行给我们。
所以未来所有新开的环境都会加载我们修改的内容。

ipython3和python3的区别
```
1.自动补全
2.支持一些bash命令
```
常用命令
```bash
系统状况
top：查看前几个进程的信息（Linux的任务管理器）
打开后，输入M：按使用内存排序
打开后，输入P：按使用CPU排序
打开后，输入q：退出
df -h：查看硬盘使用情况
free -h：查看内存使用情况
du -sh：查看当前目录占用的硬盘空间
ps aux：查看所有进程，用于查找进程
ps aux | grep match-server
kill -9 pid：杀死编号为pid的进程
传递某个具体的信号：kill -s SIGTERM pid
netstat -nt：查看所有网络连接
w：列出当前登陆的用户
ping www.baidu.com：检查是否连网
文件权限
chmod：修改文件权限
chmod +x xxx：给xxx添加可执行权限
chmod -x xxx：去掉xxx的可执行权限
chmod 777 xxx：将xxx的权限改成777
chmod 777 xxx -R：递归修改整个文件夹的权限
```
![20220604114711](https://s2.loli.net/2022/06/04/ADN1WteO4fJhx5k.png)
```bash
文件检索
find /path/to/directory/ -name '*.py'：搜索某个文件路径下的所有*.py文件
grep xxx：从stdin中读入若干行数据，如果某行中包含xxx，则输出该行；否则忽略该行。
wc：统计行数、单词数、字节数(ctrl+D结束)
既可以从stdin中直接读入内容；也可以在命令行参数中传入文件名列表；
wc -l：统计行数
wc -w：统计单词数
wc -c：统计字节数
tree：展示当前目录的文件结构
tree /path/to/directory/：展示某个目录的文件结构
tree -a：展示隐藏文件
grep xxx:统计标准输入中有多少行包含xxx
ag xxx：搜索当前目录下的所有文件，检索xxx字符串
cut：分割一行内容
从stdin中读入多行数据
echo $PATH | cut -d ':' -f 3,5：输出PATH用:分割后第3、5列数据
echo $PATH | cut -d ':' -f 3-5：输出PATH用:分割后第3-5列数据
echo $PATH | cut -c 3,5：输出PATH的第3、5个字符
echo $PATH | cut -c 3-5：输出PATH的第3-5个字符
sort：将每行内容按字典序排序
可以从stdin中读取多行数据
可以从命令行参数中读取文件名列表
xargs：将stdin中的数据用空格或回车分割成命令行参数
find . -name '*.py' | xargs cat | wc -l：统计当前目录下所有python文件的总行数
查看文件内容
more：浏览文件内容,展示部分内容
回车：下一行
空格：下一页
b：上一页
q：退出
less：与more类似，功能更全
回车：下一行
y：上一行
q：退出
head -3 xxx：展示xxx的前3行内容
同时支持从stdin读入内容
tail -3 xxx：展示xxx末尾3行内容
同时支持从stdin读入内容
用户相关
history：展示当前用户的历史操作。内容存放在~/.bash_history中
工具
md5sum：计算md5哈希值
可以从stdin读入内容
也可以在命令行参数中传入文件名列表；
time command：统计command命令的执行时间
ipython3：交互式python3环境。可以当做计算器，或者批量管理文件。
! echo "Hello World"：!表示执行shell脚本
watch -n 0.1 command：每0.1秒执行一次command命令
tar：压缩文件
tar -zcvf xxx.tar.gz /path/to/file/*：压缩
tar -zxvf xxx.tar.gz：解压缩
diff xxx yyy：查找文件xxx与yyy的不同点
安装软件
sudo command：以root身份执行command命令
apt-get install xxx：安装软件
pip install xxx --user --upgrade：安装python包
```
# 九、云服务器
![20220604163244](https://s2.loli.net/2022/06/04/BS1FO6JWCwGbdUy.png)

# 十、docker
![20220605103435](https://s2.loli.net/2022/06/05/W7eyZON6IjMQHhE.png)
为了避免每次使用docker命令都需要加上sudo权限，可以将当前用户加入安装中自动创建的docker用户组：
```bash
sudo usermod -aG docker $USER
```
## 镜像
```bash
docker pull ubuntu:20.04：拉取一个镜像
docker images：列出本地所有镜像
docker image rm ubuntu:20.04 或 docker rmi ubuntu:20.04：删除镜像ubuntu:20.04
docker [container] commit CONTAINER IMAGE_NAME:TAG：创建某个container的镜像
docker save -o ubuntu_20_04.tar ubuntu:20.04：将镜像ubuntu:20.04导出到本地文件ubuntu_20_04.tar中
docker load -i ubuntu_20_04.tar：将镜像ubuntu:20.04从本地文件ubuntu_20_04.tar中加载出来
```
## 容器
每个容器是一个完全独立的云服务器
```bash
docker [container] create -it ubuntu:20.04：利用镜像ubuntu:20.04创建一个容器。
docker ps -a：查看本地的所有容器
docker [container] start CONTAINER：启动容器
docker [container] stop CONTAINER：停止容器
docker [container] restart CONTAINER：重启容器
docker [contaienr] run -itd ubuntu:20.04：创建并启动一个容器
docker [container] attach CONTAINER：进入容器
先按Ctrl-p，再按Ctrl-q可以挂起容器
docker [container] exec CONTAINER COMMAND：在容器中执行命令
docker [container] rm CONTAINER：删除容器
docker container prune：删除所有已停止的容器
docker export -o xxx.tar CONTAINER：将容器CONTAINER导出到本地文件xxx.tar中
docker import xxx.tar image_name:tag：将本地文件xxx.tar导入成镜像，并将镜像命名为image_name:tag
docker export/import与docker save/load的区别：
export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
save/load会保存完整记录，体积更大
docker top CONTAINER：查看某个容器内的所有进程
docker stats：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息
docker cp xxx CONTAINER:xxx 或 docker cp CONTAINER:xxx xxx：在本地和容器间复制文件
docker rename CONTAINER1 CONTAINER2：重命名容器
docker update CONTAINER --memory 500MB：修改容器限制
```
```bash
scp /var/lib/acwing/docker/images/docker_lesson_1_0.tar server_name:  # 将镜像上传到自己租的云端服务器
ssh server_name  # 登录自己的云端服务器

docker load -i docker_lesson_1_0.tar  # 将镜像加载到本地
docker run -p 20000:22 --name my_docker_server -itd docker_lesson:1.0  # 将容器的22端口映射为本地的20000，因本地的22端口已用于ssh登录。再去云平台控制台中修改安全组配置，放行端口20000。

docker attach my_docker_server  # 进入创建的docker容器
passwd  # 要想ssh登录，先要设置root密码

ssh root@xxx.xxx.xxx.xxx -p 20000  # 将xxx.xxx.xxx.xxx替换成自己租的服务器的IP地址
```
```
报错：kex_exchange_identification: read: Connection reset by peer
解决：重启服务器
```
最后配置ssh免密和tmux


---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)
2.[acwing linux基础课](https://www.acwing.com/activity/content/57/)