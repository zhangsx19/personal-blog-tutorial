---
title: kali虚拟机安装与配置
date: 2022-04-10 15:41:22
categories:
- CS
tags:
- kali
- vmware
toc: true
---
**摘要：本文实现了利用虚拟机从零开始安装和配置kali系统**
<!-- more -->
---
# 一.安装和配置必要依赖
## 1、VMWARE
每个虚拟机都有独立的CMOS、硬盘和操作系统，可以像使用实体机一样对虚拟机进行操作。
在安装时，勾选增强型
![20220410163905](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410163905.png)
如果是第一次安装，启动的时候会要求打开虚拟化的设置。可参照[启动BIOS的虚拟化设置](https://jingyan.baidu.com/article/ab0b56305f2882c15afa7dda.html)
### 网络
```
vmnet1是为host-only方式服务的，vmnet8是为NAT方式服务的。
使用Host-Only模式的guest系统与主机通信需要VMnet1网卡
通过NAT方式上网的guest系统与主机通信需要VMnet8网卡
使用桥接模式上网需要网络中存在DHCP服务器，且提供服务。
```
如果发现ping不通，很可能是windows开了防火墙(公用)
```
仅主机模式：本机与新安装的虚拟机互通，但是虚拟机与其他的虚拟机互通不了。
NAT模式：本机与新安装的虚拟机互通，虚拟机与虚拟机之间也互通，但是外界访问不了你。
桥接模式：本机与新安装的虚拟机互通，虚拟机与虚拟机之间也互通，外界也能访问你这个虚拟机。(直接连接物理网络)
```
### 快照
快照是虚拟机最强大的功能，能够让你保留虚拟电脑的某一时刻。  --> 存档的意思
### 查看-立即适应客户机
如果没有说明要安装vmware tools，直接在`虚拟机`按钮处安装
### 建立共享文件夹
注意必须先在kali中[设置好](https://www.cnblogs.com/freedom-try/p/11669853.html)，再在vm里设置共享文件夹，否则会被删掉
### 远程连接
首先要开启允许远程控制(Kali不像windows,默认是没有远程桌面服务的,如果需要的话得自己安装)，然后在主机运行栏输入`mstsc`，输入虚拟机ipv4地址(`ipconfig`查看,kali是`ifconfig`)。
windows:网络右键->映射网络驱动器

## 2.Kali
kali就是用工具对目标进行渗透测试的。
[下载地址](https://www.kali.org/downloads/),推荐下载Kali Linux 64-Bit VMware VM(这个版本是专门用于Vmware)。(网页查找VMWARE即可)。解压后找到vmx文件用虚拟机打开。可以选择编辑虚拟机设置。打开后选择我已移动该虚拟机(点复制有些工具可能会路径错误)。
![20220410154827](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410154827.png)
开机输入默认的账户和密码，都为kali（2021.1以后和之前的老版本不同，只是一个`普通用户`,老版本为root用户，账户和密码均为root）
![20220411212435](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220411212435.png)
如何删除虚拟机：选中要删除的虚拟机操作系统，单击右键，选择 “管理” 选项。然后在选择 “从磁盘中删除” 选项即可删除该虚拟机操作系统
# 二、设置root用户
这里我们可以直接更改root用户的密码，后续就可以用root用户登陆了
切换到root权限：`sudo su`
打开终端，输入命令：`sudo passwd root`
![20220410155225](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410155225.png)
提示输入kali用户的密码，kali的默认密码为kali。接下来输入新密码，输入两遍新密码之后，root用户的密码成功修改。接下来可以重启kali 用root用户登录，并且输入上面步骤的新密码。重启命令：`sudo reboot`
# 三、设置中文
## （1）设置中文编码
命令：`dpkg-reconfigure locales`

![20220410160317](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410160317.png)
进入选择语言的图形化界面之后，（空格是选择，Tab是切换）
选中 en_US.UTF-8、zh_CN.GBK、zh_CN.UTF-8、zh_CN.GBK，图为初始界面，界面下选项，可以下拉，排序为从a-z排序。
![20220410161424](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410161424.png)
回车之后，会让你设置默认编码，设置成zh_CN.UTF-8，回车。
![20220410161859](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410161859.png)
注意：重启后要选择`保留旧的名称`，方便以后的配置。
![20220411213409](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220411213409.png)

## （2）配置源
不然下载软件的时候会比较慢，源可以理解为软件的仓库
做一下备份：`sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup`,如果以后源列表无意毁坏了，可以恢复一下:`sudo cp /etc/apt/sources.list_backup /etc/apt/sources.list`
打开源文件：`vim /etc/apt/sources.list`。此时文件里面只有一个官方源，建议注释，不然还是会使用这个源。vi和vim都是Linux中的编辑器，vi使用于文本编辑,但是vim适用于coding和文本。
![20220410155735](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410155735.png)

推荐源：
```
# kali官方源
deb http://http.kali.org/ moto main non-free contrib
deb-src http://http.kali.org/ moto main non-free contrib
deb http://security.kali.org/ moto/updates main contrib non-free
deb-src http://security.kali.org/ moto/updates main contrib non-free
```
接着更新源，命令：
```
apt-get update #更新一下源
sudo apt-get dist-upgrade -y #更新系统和软件
#这里最好快照一下
sudo apt-get autoremove -y #清理安装包
reboot #重启
```
更新源时，如果出现以下错误，换个源
![20220413131208](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413131208.png)
如果中间出错了，会提示执行`apt --fix-broken install`,再执行即可。
![20220410155911](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220410155911.png)
更新好就会有这个，选择yes
![20220411233815](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220411233815.png)

## （3）安装中文输入法
命令：`apt-get install fcitx fcitx.googlepinyin`,重启后在搜索框搜索“fcitx”,点击“fcitx配置”程序，将Google输入法调在第一位即可
切换：ctrl+空格
## （4）安装中文字体
如果使用chrome浏览器,发现中文显示全是方框。而系统自带的firefox却没有这个问题,原因是系统缺少相应的字体库支持
命令：`sudo apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy`
安装完后输入`sudo reboot`重启，记得在登陆界面选择中文，再登陆,则汉化完成。
## 5）浏览器改为中文
kali默认浏览器是网络浏览器，点击search for more languages;select a language to add,找到Chinese(China),点击add。
![20220413143238](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413143238.png)

## 6）浏览器安装插件
在扩展和主题里，安装omega代理插件，应用选项如下
![20220413143704](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413143704.png)
![20220413143822](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413143822.png)

# 三、安装JDK1.8并且切换(不一定要切换)
kali默认的java版本是，版本过高不太稳定，较稳定的版本是JDK1.8。
先把包拖进虚拟机

```
解压安装包：tar -axvf jdk-8u311-linux-x64.tar.gz
将文件移动到opt目录再改名为java：mv ./jdk1.8.0_311 /opt/java
```

	编辑：vi /etc/profile
	export JAVA_HOME=/opt/java
	export PATH=$PATH:$JAVA_HOME/bin
	export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
	export JRE_HOME=$JAVA_HOME/jre

![20220413144429](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220413144429.png)
```
更新：source /etc/profile
更新完后会出现#,关掉终端，再打开一个命令行
切换：
update-alternatives --install /usr/bin/java java /opt/java/bin/java 3
update-alternatives --config java #切换回去也是这条命令
选择1
java -version #查看版本
```
# 四、踩过的坑
## 1.更新时卡住了，只能退出重来，结果提示
```
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```
这些错误提示一般都是因为某些程序在系统后台进行着某些 apt 操作，因此锁定了 apt 数据库，所以暂时不能进行 apt 操作。
遇到这种情况，一般我们只需要安静地等待几分钟。直到当前的更新、安装或卸载任务完成后，锁就会自动释放，然后就可以进行 apt 操作了。
非正常情况下，比方说你等了好多个几分钟锁都还没有被释放，你就要看看是不是该进程由于某些原因而卡住了并且一直占用着锁。如果是的话，那你只能干掉这个进程，然后删除该锁定了
首先，我们先找出是哪个进程占用了锁文件 /var/lib/dpkg/lock
```
sudo lsof /var/lib/dpkg/lock-frontend #sudo lsof 文件
```

![20220412003216](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220412003216.png)
我们可以从结果中看到，该进程的 PID 为 1548。接着，kill 掉这个进程
```
sudo kill -9 1548
```
然后你就可以放心地删除锁文件
```
sudo rm /var/lib/dpkg/lock
sudo rm /var/cache/apt/archives/lock #删除缓存目录下的锁文件
sudo dpkg --configure -a
```
## 2.更新源时release仓库过期
首先确保虚拟机与主机的时间是同步的(虚拟机-设置-选项-VMWARE TOOLS)，如果还是不行，可能是长时间挂着虚拟机，时间不同步了，只需重启下即可

---
# 总结
经历千辛万苦终于安装和配置成功，接下来开始学习了。

---
# 参考资料
1.[kali2021.4软件更新以及输入法安装](https://bbs.zkaq.cn/t/6253.html)
2.[更新卡住解决_Linux安装软件时90%的人会遇到这个报错，如何解决？](https://blog.csdn.net/weixin_42356349/article/details/112610893)