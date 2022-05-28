---
title: sqlmap的ip黑名单绕过
date: 2022-04-16 00:02:42
categories:
- CS
- security
tags:
- spider
- redis
- proxypool
- tor
- socks5
toc: true
---
**摘要：本文提出了两种sqlmap绕过ip黑名单的方法。分别是基于github上的ProxyPool项目搭建自己的免费代理池，和基于tor实现ip实时变化。**
<!-- more -->
# 前言
做靶场的sql注入时因访问频率过高被禁ip,就想实现一个不停变换ip的sqlmap。一开始想到用代理，结果在配置时踩了无数坑，且免费代理的效果和安全性也不太好，转而用tor。

---
# 一、基于proxypool搭建代理池
## 1.安装和配置必要依赖
## (1)redis服务
Redis是由C语言编写的开源、基于内存、支持多种数据结构、高性能的Key-Value数据库。

安装redis
```
wget https://download.redis.io/releases/redis-6.2.6.tar.gz //2022.4 最新
tar xzf redis-6.2.6.tar.gz
mv redis-6.2.6 /usr/local/redis
cd /usr/local/redis
make
make install PREFIX=/usr/local/redis
```
安装完成的提示

![20220417135725](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417135725.png)

启动redis
```
vim /bin/redis.conf //需在redis安装目录执行,将该配置文件中的daemonize no改为daemonize yes,来redis以后台方式运行
./bin/redis-server redis.conf
ps -ef | grep redis//查看redis进程
./bin/redis-cli
set test hello
get test//测试
exit
```
![20220417140213](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417140213.png)
![20220417140101](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417140101.png)

## (2)proxypool
[github上的15k stars项目proxypool](https://github.com/jhao104/proxy_pool)，主要功能为定时采集网上发布的免费代理验证入库，定时验证入库的代理保证代理的可用性，提供API和CLI两种使用方式。
```bash
git clone https://github.com/jhao104/proxy_pool.git
pip install -r requirements.txt
更新配置setting.py(主要是改API的PORT和数据库)。
如：PORT = 5010                    # 监听端口
DB_CONN = 'redis://:pwd@127.0.0.1:8888/0'
python proxyPool.py schedule # 启动调度程序
python proxyPool.py server # 启动webApi服务
```
执行proxypool项目的调度程序和webApi服务程序(调度程序执行到base.py就可退出，但webApi需一直执行才能访问api网站)，然后访问setting里的127.0.0.1:PORT,(PORT为setting中设置的值，如默认的5010)，然后会提示访问不同文件的功能，如访问http://127.0.0.1:5010/get是获得一个代理地址。如下

![20220416181916](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220416181916.png)

如图，我们发现它的响应有很多属性，甚至还保留了属性名，而要使用sqlmap的--proxy代理功能需要网站只返回一个代理的地址
实现方法是把127.0.0.1:5010/all里的所有代理ip采集下来并存在ips.txt中,再转发至127.0.0.1的一个端口IPSPORT，然后设置代理=127.0.0.1:IPSPORT

把/all里的ip采集到ips.txt并通过亚马逊ip验证
```python
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/all").json()

res = requests.get("http://127.0.0.1:5010/count").json()
count = res["count"]["total"]
print("目前代理池中共计：%s个代理." % count)

f = open("ips.txt", "w")
ipall = get_proxy()#注意不能在for里面用这个函数，否则会list越界(count变化)
for i in range(count):
    b = ipall[i]["proxy"]
    try:
        requests.get('http://checkip.amazonaws.com/', proxies={"http": "http://{}".format(b)},timeout=0.5)#需要快速响应的ip
        print(i)
        f.write(b + "\n")
    except Exception:
        pass
f.close()

```
autoproxy需修改下except，代理为http://127.0.0.1:50007。只要ip池足够大，连接失败会自动切换可用ip
```
print(a)
 except Exception:
    local_server.close()
    logger.debug('Stop mapping service.')
    break
```

# 二、基于tor实现sqlmap或浏览器ip实时变化
## 1.基于tor browser
### (1)安装tor browser
安装tor browser解压包，进入解压后的目录 tor-browser_en-US 中打开 Browser 文件夹，找到 start-tor-browser 文件，编辑文件，将图中的0改为1，然后保存，目的是能用root用户使用tor(tor不推荐用root权限使用)

![20220417153701](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417153701.png)

然后退出 Browser 文件夹选择 start-tor-browser.desktop 点击运行会出现如下界面，在配置中输入梯子的HTTP地址和端口

![20220417153829](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417153829.png)

连接 Tor 服务器成功,即可使用
### (2)配置proxychain
kali自带proxychain4,可配置tor代理命令的地址和端口

先查看 Tor 在主机上的服务端口，如图默认是9150(注意保持tor浏览器打开)

![20220417154018](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417154018.png)

`locate proxychains.conf`查找 proxychains.conf位置,修改 proxychains.conf 文件,然后用`proxychains curl ipconfig.me`测试是否代理成功

![20220417154100](https://cdn.jsdelivr.net/gh/zhangsx19/PicBed/images_for_blogs20220417154100.png)

### (3)修改tor browser配置
tor浏览器除了第一次访问某网站会分配给你一个和主机不同的ip，好像是默认10分钟换一次ip的。不能满足我们sqlmap的需求，可以在Browser/TorBrowser/Data/Tor/修改torrc配置文件，只需加上一行
```
MaxCircuitDirtiness 1
```
可以改成每1分钟换一次ip

## 2.基于tor和ipchanger
### (1)安装docker
Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的镜像中，然后发布到任何流行的 Linux或Windows操作系统的机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口
```bash
curl  -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo 'deb https://download.docker.com/linux/debian stretch stable'> /etc/apt/sources.list.d/docker.list
apt-get install apt-transport-https  ca-certificates  curl  gnupg2  software-properties-common
apt-get update 
sudo apt install docker.io #安装docker
docker -v #检查是否安装成功
apt install docker-compose #安装docker compose
输入docker-compose,显示可用命令，则安装成功
```
### (2)安装tor
终端输入tor按照提示下载即可，下载完再次输入tor，显示正在建立链接(需梯子)，其默认端口为9050(查看方法同上)。

如果要配置tor代理的话同上，不配置也可用SOCKS5代理直接用

### (3)安装ipchanger
[ipchanger](https://github.com/seevik2580/tor-ip-changer)通过使用 TOR服务端每隔10秒请求一次新身份，可实现10秒换1次ip

Linux只能用docker安装，安装方法
```
把整个项目下载下来,解压到ipchanger文件夹
进入Dockerfile同级目录
docker build . -t ipchanger
xhost +
docker run -p 14999:14999 -p 9050:9050 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix ipchanger
然后就先start tor server(可以不开tor，但要梯)
start IP change
```
默认代理端口为9150，可通过proxychain查看tor服务获得
# 三、sqlmap绕过ip黑名单
用sqlmap扫描目标网址总是被封，该怎么利用以上方法呢？
```
sqlmap -u "" –-proxy= http://127.0.0.1:5000
sqlmap -u "" --proxy= socks5://127.0.0.1:9150
sqlmap -u "" --tor -tor-type=SOCKS5
```

使用之前先检测一下[代理是否会变化](https://checkip.amazonaws.com/)

# 遇到的问题
OSError: [Errno 98] Address already in use 错误是指端口被占用，未释放或者程序没有正常结束
```
lsof -i:端口号 #可通过端口号来查找进程ID
kill -9 pid #pid是指进程的ID号 ，kill -9 用来强制杀死进程
```
---
# 总结
免费代理还是比较少的，而且匿名性也不好，有条件还是得用付费代理。

---
# 参考资料
1. [Linux上安装Redis教程](https://baijiahao.baidu.com/s?id=1722728002073366376&wfr=spider&for=pc)

2. [ProxyPool文档](https://proxy-pool.readthedocs.io/zh/latest/user/how_to_use.html)

3. [SqlMap代理池](https://www.cnblogs.com/AtSunset/p/15144553.html)

4. [Sqlmap自动切换代理](https://cloud.tencent.com/developer/article/1535219)

5. [luminati代理快速使用教程](https://www.cnblogs.com/jhao/p/15611785.html)

6. [如何配置 Tor 代理池以及实现Sqlmap渗透注入防封IP测试](https://blog.csdn.net/haduwi/article/details/119395502)

7. [kali安装docker（亲测有效）](https://blog.csdn.net/aodechudawei/article/details/122450720)

8.  [dockerfile菜鸟教程](https://www.runoob.com/docker/docker-dockerfile.html)

9. [sqlmap笔记](https://xlmy.net/2017/09/08/Spring%E5%88%9D%E5%AD%A6%E7%AC%94%E8%AE%B0/)