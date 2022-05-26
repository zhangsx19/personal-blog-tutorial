---
title: python_scrapy
date: 2022-05-25 16:58:50
categories:
- CS
- security
tags:
- scrapy
- python
toc: true
---
**摘要：本文介绍了爬虫项目**
<!-- more -->
# 安装依赖
```bash
pip install lxml
conda install bs4
```
---
# 一.前置知识
爬虫在使用场景中的分类
- 通用爬虫：
    抓取系统重要组成部分。抓取的是一整张页面数据。
- 聚焦爬虫：
    是建立在通用爬虫的基础之上。抓取的是页面中特定的局部内容。
- 增量式爬虫：
    检测网站中数据更新的情况。只会抓取网站中最新更新出来的数据。

http协议
- User-Agent：请求载体的身份标识
- Connection：请求完毕后，是断开连接还是保持连接
![20220525120443](https://s2.loli.net/2022/05/25/tSLvVa7fPGCoTRy.png)

# 二、requests库
```py
#step_1:指定url
#step_2:发起请求
#step_3:获取响应数据.text返回的是字符串形式的响应数据
#step_4:持久化存储
```
## 翻译
页面局部刷新->ajax请求

# 三、数据解析
## 1.正则解析
```html
<div class="thumb">
<a href="/article/121721100" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12172/121721100/medium/DNXDX9TZ8SDU6OK2.jpg" alt="指引我有前进的方向">
</a>
</div>
```
```py
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
```
## 2.bs4
    - 数据解析的原理：
        - 1.标签定位
        - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理：
        - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装：
        - pip install bs4
        - pip install lxml
    - 如何实例化BeautifulSoup对象：
        - from bs4 import BeautifulSoup
        - 对象的实例化：
            - 1.将本地的html文档中的数据加载到该对象中
                    fp = open('./test.html','r',encoding='utf-8')
                    soup = BeautifulSoup(fp,'lxml')
            - 2.将互联网上获取的页面源码加载到该对象中
                    page_text = response.text
                    soup = BeatifulSoup(page_text,'lxml')
        - 提供的用于数据解析的方法和属性：
            - soup.tagName:返回的是文档中第一次出现的tagName对应的标签
            - soup.find():
                - find('tagName'):等同于soup.div
                - 属性定位：
                    -soup.find('div',class_/id/attr='song')
            - soup.find_all('tagName'):返回符合要求的所有标签（列表）
        - select：
            - select('某种选择器（id，class，标签...选择器）'),返回的是一个列表。
            - 层级选择器：
                - soup.select('.tang > ul > li > a')：>表示的是一个层级
                - oup.select('.tang > ul a')：空格表示的多个层级
        - 获取标签之间的文本数据：
            - soup.a.text/string/get_text()
            - text/get_text():可以获取某一个标签中所有的文本内容
            - string：只可以获取该标签下面直系的文本内容
        - 获取标签中属性值：
            - soup.a['href']
## 3.xpath
xpath解析：最常用且最便捷高效的一种解析方式。通用性。

    - xpath解析原理：
        - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
    - 环境的安装：
        - pip install lxml
    - 如何实例化一个etree对象:from lxml import etree
        - 1.将本地的html文档中的源码数据加载到etree对象中：
            etree.parse(filePath)
        - 2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        - xpath('xpath表达式')
    - xpath表达式:
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
        - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有的文本内容）
        - 取属性：
            /@attrName     ==>img/src

---
# 总结

