---
title: 用HEXO从零开始搭建个人博客
---
**摘要：一篇如何使用Github Pages和Hexo搭建自己的个人博客的教程，里面介绍了如何使用和配置Hexo框架，如何将Hexo部署到自己的Github项目中，如何注册域名以及将自己的域名关联到Github Pages上。**



# 前言
一直想搭建一个属于自己的博客，一方面可以记录自己的学习成果和技术理解，一方面在面试中也是加分项。在此记录下首次搭建个人博客的踩坑之路。

---


# 一、技术选型
## 1.为什么选择HEXO？

博客生成技术分为静态和动态网站生成，考虑到静态相比动态生成，有如下优点：
 1.内容存储为平面文件，因此不需要数据库
 2.静态网站不需要动态服务器端处理
 3.静态网站比动态网站超快，因为它们不需要服务器端处理或数据库访问
 4.静态网站比任何动态网站都更安全，因为可以利用的安全漏洞更少
 5.缓存静态文件比缓存动态页面更有效

所以本次使用静态生成，目前主流静态站点生成器有：Hexo和Hugo等，Hugo是一个用Go语言构建的静态站点生成器，其搭建较简单但可扩展性差。而Hexo是基于Node的开源静态生成器，有以下优点：
 1.构建速度快
 2.使用一个部署命令可部署到Github或其他任何主机
 3.强大的Markdown支持
 4.高度可扩展
 5.丰富的开源主题与插件
 
 基于此，本次采用Hexo进行博客搭建。
 
## 2.为什么选择Github-Pages
Github Pages是用户编写的、托管在github上的静态网页,优点有：
1.可以绑定你的域名
2.简单快捷，可以提供一个免费的服务器，免去了自己搭建服务器和写数据库的麻烦。

# 二、搭建步骤
## 1.安装和配置必要框架
### Git安装
去[Git官网](https://git-scm.com/download/win)根据你的电脑参数，下载对应版本并安装。
安装完成后在桌面或任意文件夹点击鼠标右键，会有`Git GUI Here`和`Git Bash Here`两个按钮，一个是图形界面的Git操作，一个是命令行。
一般选择命令行操作`Git Bash Here`。
<img src="https://img-blog.csdnimg.cn/0f8976ee9b714d83a981e9cf1bf0fcce.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_left" width = "200" height = "200" alt="" align=center />

### Node.js安装
到[官网](https://nodejs.org/en/download/)根据电脑参数下载安装文件并执行，无脑点下一步即可，无需配置环境变量，完成安装。
### Hexo安装与配置
桌面右键鼠标，点击`Git Bash Here`，输入以下命令即可安装。
```
npm install hexo-cli -g   
npm install hexo-deployer-git --save
```
第一句是安装hexo，第二句是安装hexo部署到git page的deployer，两个都需要安装。如下图即安装完成。

<img src="https://img-blog.csdnimg.cn/bfb32acb28ec412c926ccc20971b53f3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

安装完成后，根据自己喜好创建一个Hexo文件夹(如D:\Blog\Hexo),<font color='red'>进入创建的文件夹目录</font>，右键鼠标，点击`Git Bash Here`，执行命令:
```
hexo init     
```
Hexo 将在指定文件夹中新建所需要的初始化配置文件，如下图
<img src="https://img-blog.csdnimg.cn/3c701ec12c184fbfa303f75ce99a581b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

```
hexo clean 	  #清理缓存
hexo generate #进行渲染 简写为 hexo g
hexo server   #部署到本地(调试使用) 简写为 hexo s
```
终端中会出现`INFO  Hexo is running at http://localhost:4000/`。
此时在浏览器输入网址[http://localhost:4000](http://localhost:4000)，即可查看本地的效果，如下图
<img src="https://img-blog.csdnimg.cn/b2ebc36c1fa84661a59b1d619659b8aa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

此时个人博客初步创建成功，但这是本地调试用的，其他人看不到(调试完毕后记得在git命令行中Ctrl+C来停止运行，不然下次就进不去了)，所以接下来我们需要把它部署到服务器上，从而让每个人都能通过互联网访问到我们的个人博客。

<img src="https://img-blog.csdnimg.cn/a69b07d277654812b81f15a72be1ccf4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

## 2.将博客部署到Github-Pages上
### 在Github中创建github.io项目代码库
注意repository的名字必须是：你的用户名.github.io
### 将本地的Hexo文件更新到Github的库中
打开创建的Hexo文件夹，修改配置文件_config.yml 
以后的大部分操作都会在_config.yml中进行，它是站点的配置文件。
在Hexo文件夹下,右键鼠标，点击`Git Bash Here`,执行命令：

```
hexo clean    	#清理缓存
hexo generate   #进行渲染 简写为 hexo g
hexo server 	#部署到本地 简写为 hexo s 可省略
hexo deploy 	#部署到git服务器  简写为 hexo d
```
以上代码为了简单后续统称为“更新代码”，即每次在本地进行了操作（如修改了配置、新写或修改了博客文章等),都需执行“更新代码”来同步到git服务器，从而让别人浏览到。其中`hexo s`命令<font color='red'>也可省略</font>，即如果没有本地调试需求，可以直接commit到git服务器。
如报错`ERROR Deployer not found: git`,deployer没有安装成功，需要执行如下命令再安装一次：
```
npm install hexo-deployer-git --save
```
再执行`hexo g -d`，出现`INFO  Deploy done: git`即部署成功，在浏览器上输入Github Pager为我们生成的外链：你的用户名.github.io（如[zhangsx19.github.io](https://zhangsx19.github.io/)），即可看到自己的博客，且每个人都可通过此地址访问到。

# 三、写第一个博客
搭好博客后，进入创建的Hexo文件夹，使用如下命令来新建文章：

```
hexo new post “文章名字” #简写为 hexo n "文章名字"
```

建立好的文章存储在./source/_posts 中，你可以在本地用<font color='red'>markdown</font>语法编辑内容。编辑完成后还需要<font color='red'>执行“更新代码”</font>
```
hexo clean
hexo g
hexo d   #可与hexo g合并为 hexo d -g
```
再刷新浏览器就可看到新文章。如下图:
<img src="https://img-blog.csdnimg.cn/07b2e9957fde4ad280a8cee1d8e62bbf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

# 四、将域名关联到Github Pages(可选）
## 1.域名购买
如果不想用github提供的免费域名，可以选择在[阿里云](https://wanwang.aliyun.com/domain/?spm=5176.383338.1907008.1.LWIFhw)上买一个属于自己的域名，然后将自己域名绑定到自己的Github Pages博客上
## 2.域名解析
购买域名并实名认证后，需要把域名解析到我们的博客中，在阿里云的域名控制台找到域名右侧对应的解析按钮。点击添加解析，然后按照如下填写添加解析，记得把记录值替换成你自己的博客地址。

<img src="https://img-blog.csdnimg.cn/bda55944890b41008afb4b6e5ecd5095.png#pic_center" width = "400" height = "400" align=center />
<img src="https://img-blog.csdnimg.cn/7557c1f1b73e4dc78fbad1c6e7baefd2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width = "400" height = "400" align=center />

之后记得启用该记录。
## 3.博客配置
购买域名后，在Hexo\source 文件夹下创建文件 CNAME （通过记事本创建和打开，没有后缀名），内容为你的域名，如[sx-zhang.top](http://sx-zhang.top/)。
![在这里插入图片描述](https://img-blog.csdnimg.cn/5be112bf7343479586dc6b88143ebcff.png#pic_center)

然后在Hexo文件夹执行“更新代码”。

```
hexo clean
hexo g -d
```
就可以通过购买的域名访问博客了。如果不能访问可能是因为运营商DNS缓存问题。等几分钟就可以。

# 五、实现https协议(可选）
购买的域名是http协议，如果用google浏览器或者Safari，会提示网站不被信任，只有你点击仍要继续才会展示你的博客。而使用https协议就不会有这个问题，有以下方法：
1. 购买证书
2. 使用免费CA证书。腾讯云阿里云都有提供。不过有时间限制
3. 使用CDN进行反向代理

因为我们使用的github Page是不支持上传证书的，所以此次使用第三种:通过CDN配置反向代理。
## 原理
[Cloudflare](https://www.cloudflare.com/zh-cn/) 提供DNS解析服务，而且速度很快。它提供了免费的https服务(但不是应用SSL证书)。实现模式是，用户到CDN服务器的连接为https，而CDN服务器到GithubPage服务器的连接为http，即在CDN服务器那里加上反向代理。

## 步骤
去官网注册后添加购买的域名，进入DNS解析界面填入如下解析：
![在这里插入图片描述](https://img-blog.csdnimg.cn/0f0afa3cc54b4f3c81142232c446147e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

其中前两个是使你的域名指向github的服务器地址(github文档中给的)，最后CNAME记录指向的是github仓库域名username.github.io。一定要严格按照这个来配置。
记录下cloudflare给你的DNS解析服务器，就在上一步那个页面下边，用这个记录去把阿里云的DNS解析服务器替换掉，同时删掉阿里云里面的DNS解析记录，因为只靠clouleflare来解析DNS。

![在这里插入图片描述](https://img-blog.csdnimg.cn/1a3badcf4ce1428e8420231c23393a4f.png#pic_center)
回到clouldflare上面选择SSL/TLS的Overview选项，然后选择Full或者是Flexible。再在Edge Certificates里打开always use HTTPS开关。
此时即可用https访问个人博客啦！

![在这里插入图片描述](https://img-blog.csdnimg.cn/c1c00d606dbf48de8f3e0b94ee6ddf72.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAemhhbmdfX3N4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
坑点：博文不能有<font color='red'>非https的链接</font>，比如图片图床不能是https的，或者评论插件不支持https等


---
# 总结
本文简单介绍了如何用Hexo框架从零开始搭建属于自己的个人博客，以及如何把购买的域名关联到Github Pages,并利用CDN配置反向代理实现https协议。
搭建完博客后，接下来就是要个性化个人博客和学习Markdown来写博客了。

想了解更多，欢迎来参观我的博客：[Zhangsx’s Blog](https://sx-zhang.top/) 和github：[zhangsx19](https://github.com/zhangsx19?tab=repositories)

---

# 参考资料
1. [hexo搭建博客以及域名解析分析](https://juejin.cn/post/6844903720296120328)

2. [2018，你该搭建自己的博客了！](https://juejin.cn/post/6844903549646667789)
3. [关于HEXO搭建个人博客的点点滴滴](https://juejin.cn/post/6844903557070602254#heading-6)