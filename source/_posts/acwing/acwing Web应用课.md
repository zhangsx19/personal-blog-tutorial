---
title: acwing web应用课
date: 2022-04-14 10:35:24
categories:
- acwing
tags:
- html
- css
- js
- React
- Vue3
toc: true
---
**摘要：acwing web应用课学习笔记**
<!-- more -->
# 一、安装与依赖
## vscode
插件：Live Server(一般网站都是部署在linux服务器上，linux会有服务来承载我们的网站，可以帮我们模拟一个网站的后端服务器，本地搭建网站->open with live server)
auto rename tag(修改标签头时可以自动修改尾)
保存时自动对齐格式化:设置->搜索format on save

技巧：ctrl+/ 注释掉光标所在的行，再按一下就是取消注释
## MDN WEB DOCS

# 二、html
## 1.html文件结构
有些标签是没有结束标签的，如meta
body是承载网站内容的地方
![20220517192154](https://s2.loli.net/2022/05/17/ksg9tmWujRVPD6v.png)
第一行写文件类型
快速补全:不用打括号，直接tab括号里的内容(更简便的是直接输一个！)

## 2.文本标签
绝大部分标签都是div和span扩展出来的，只是用了不同的CSS样式
div是一个块，把内容归到一起，方便css和js操作,默认换行
```
其他块级标签例如：<h1>, <p>, <pre>, <ul>, <ol>, <table>
```
span是行内元素，默认不带回车
![20220519172253](https://s2.loli.net/2022/05/19/Ijf5t4PGFRghmlr.png)
```
其他内联标签例如：<i>, <b>, <del>, <ins>, <td>, <a>
<img>
```
&nbsp是空格 br是回车
hr是加一条水平线

## 3.表单
form标签
表示文档中的一个区域，此区域包含交互控件，用于向 Web 服务器提交信息。
form内的button会把form的所有内容都提交

# 三、css
## 1.样式定义方式

## 2.选择器

## 3.颜色

## 4.文本

## 5.字体

## 6.背景
## 7.边框

## 8.元素展示格式

## 9.内边距与外边距
## 10.盒子模型
#
## 12.浮动
## 13.flex布局
## 14.响应式布局

# 四、js(ES6标准)
使用方式
HTML页面中的任意位置加上`<script type="module"></script>`标签即可。
常见使用方式有：
```html
直接在<script type="module"></script>标签内写JS代码。
直接引入文件：<script type="module" src="/static/js/index.js"></script>。
将所需的代码通过import关键字引入到当前作用域。
```
```js
<script type="module">//严格限制变量作用域
    import { name, print } from "/static/js/index.js";

    console.log(name);
    print();
</script>
```
CSS控制HTML
JavaScript控制HTML与CSS
执行顺序：和渲染html页面一样，从上到下依次执行
## 1.输入与输出
===和！==和php的弱类型比较一样
和前端的交互：
一般把script放下面，为了防止执行脚本的时候页面内容还没有渲染出来(从上到下执行)
input是一个标签
![20220520180225](https://s2.loli.net/2022/05/20/pMFPDA2ZUYc1GzH.png)
标签.addEventListener(事件，触发事件时执行的函数)作用是给某个标签绑定一个函数
从终端(标准输入)获取输入：
js文件的export提供接口
## 2.类
函数里可以用add.prototype来定义类(ES6里有了class后就不用了)
实际在前端中，每个class往往对应一个组件，复杂的组件里还可以有多个class作为成员，比如页面类里有多个按钮类作为成员
定义类的成员变量时不仅可在构造函数定义，还可在任意函数中定义
继承用extends 父类
子类的构造函数一定要先用super调用父类构造函数，再定义自己的成员变量
在其他函数调用的super是指向父类的实例
子类的函数会把父类的覆盖掉(多态)
### 静态成员(直接在前面加static)
构造类的实例时是没有初始化静态成员的，也不能调用
要通过类名去调用(只有这一种方法)
静态函数或静态变量是和类相关的，与实例无关，即并不是实例的成员
一旦静态成员改变了，对所有实例来说都改变了
应用：`this.id = ++Point.cnt;`
当静态变量较多，就可以写专门的静态函数来操作这些变量
静态成员可以被继承

## 3.事件(js和页面产生交互)
JavaScript的代码一般通过事件触发。
可以通过`addEventListener函数`为元素绑定事件的触发函数。
常见的触发函数有：
```javascript
鼠标
click：鼠标左键点击
dblclick：鼠标左键双击
contextmenu：鼠标右键点击
mousedown：鼠标按下，包括左键、滚轮、右键
    event.button：0表示左键，1表示中键，2表示右键
mouseup：鼠标弹起，包括左键、滚轮、右键
    event.button：0表示左键，1表示中键，2表示右键
键盘
keydown：某个键是否被按住，事件会连续触发 = mousedown
    event.code：返回按的是哪个键
    event.altKey、event.ctrlKey、event.shiftKey分别表示是否同时按下了alt、ctrl、shift键。
keyup：某个按键是否被释放 = mouseup
    event常用属性同上
keypress：紧跟在keydown事件后触发，只有按下字符键时触发。适用于判定用户输入的字符。 = click
    event常用属性同上
keydown、keyup、keypress的关系类似于鼠标的mousedown、mouseup、click

表单
focus：聚焦某个元素
blur：取消聚焦某个元素
change：某个元素的内容发生了改变(只有取消聚焦时才会识别是否改变)

窗口(浏览器)
需要作用到window元素上。
resize：当窗口大小放生变化
scroll：滚动指定的元素
load：当元素被加载完成

调试
event.type //可返回触发的事件类型,如click
```
## 4.常用库
```
jQuery(ajax) -获取DOM元素(比原始写法代码更短)
setTimeout与setInterval
requestAnimationFrame
Map与Set
localStorage
JSON
日期
WebSocket
window
canvas
```
### jQuery
一般变量前会有$
选择器的语法和css一样
事件：元素.on('click',function(){})
也可以直接\$div.click(function(){})
解绑定(如希望只点击一次)用.off('click'),注意写在on函数里
可以绑定多个函数(依次执行)
如何解绑部分函数：可以给事件提供一个名称，如click.name1，然后解绑对应事件
```js
在事件触发的函数中的return false等价于同时执行：function(e)
e.stopPropagation()：阻止事件向上传递
e.preventDefault()：阻止事件的默认行为
```
事件向上传递：
```js
let $div = $('div');
let $a = $('div > a')
let main = function () {
    $div.on('click', function () {
        console.log('haha');
    })
    $a.on('click', function (e) {//点a会输出a,haha
        console.log('a');
        //e.stopPropagation();//只输出a
        //e.preventDefault();//输出a,haha,但无法打开超链接
        //return false//等价于写了上面两函数,即只输出a，无法打开
    })
}
```
元素的隐藏与展现
元素的添加与删除:$(标签的完整写法) --动态添加
append是尾插，prepend是头插
```js
$A.remove()：删除元素$A
$A.empty()：清空元素$A的所有儿子
```
类的添加与删除(如点击改变颜色)
操作css
```js
$div.on('click', function () {
    console.log($div.css('background'));
    $div.css('background', 'blue');
})
$div.on('click', function () {
    console.log($div.css('background-color'));
    $div.css({
        'width': '20px',
        'background-color': 'blue'
    });
})
```
对元素属性的操作：
```js
$('div').attr('id')：获取属性
$('div').attr('id', 'ID')：设置属性
```
对元素内容的操作：
```js
$A.html()：获取、修改HTML内容
$A.text()：获取、修改文本信息
$A.val()：获取、修改文本的值 //一般用在input或textarea里
```
查找某个元素：
```js
$(selector).parent(filter)：查找父元素//length为0表示查不出来
$(selector).parents(filter)：查找所有祖先元素
$(selector).children(filter)：在所有子元素中查找
$(selector).find(filter)：在所有后代元素中查找
```
![20220521112932](https://s2.loli.net/2022/05/21/8n3KJVk1WuvayET.png)

### ajax用来和后端通信
ajax即一般的http协议，只能由客户端向服务器发送请求，然后服务器返回响应，服务器无法主动向客户端发送请求
GET方法：
```js
$.ajax({
    url: url,//后端链接
    type: "GET",
    data: {
    },
    dataType: "json",//返回内容的类型
    success: function (resp) {//如果没报错，从后端获取信息后就会调用函数，resp为后端返回的信息

    },
});
```
在不刷新页面的前提下只从服务器端获取某些数据(一般是json)
POST方法：
```js
$.ajax({
    url: url,
    type: "POST",//唯一区别 表单
    data: {//往后端传的参数 
    },
    dataType: "json",
    success: function (resp) {

    },
});
```
### 延时执行函数
```js
setTimeout(func, delay) //delay毫秒后，执行函数func()。
clearTimeout() //关闭定时器

let timeout_id = setTimeout(() => {
    console.log("Hello World!")
}, 2000);  // 2秒后在控制台输出"Hello World"
clearTimeout(timeout_id);  // 清除定时器

setInterval(func, delay) //每隔delay毫秒，执行一次函数func()。第一次在第delay毫秒后执行。
clearInterval() //关闭周期执行的函数
```
### requestAnimationFrame
页面刷新之前执行一次，通常用递归写法，使其`每秒执行60次`func函数，用于做动画或游戏
```js
let step = () => {
    requestAnimationFrame(step);//刷新时执行函数
    $div.width($div.width() + 1);//元素变了，页面就要刷新一下
}
requestAnimationFrame(step);//执行一次
```
如果执行时切换到其他页面它会暂停，原因是每一帧渲染前才会执行一次，如果页面切换了，浏览器就不会再渲染它
setTmeout两次调用之间的间隔包含回调函数的执行时间(有可能恰好在一个帧开头，就得等到下一帧才能执行，函数执行时间长时效果就会忽快忽慢)；setInterval只能保证按固定时间间隔将回调函数压入栈中，但具体的执行时间间隔仍然受回调函数的执行时间影响。
当页面在后台时，因为页面不再渲染，因此requestAnimationFrame不再执行。但setTimeout与setInterval函数会继续执行。
![20220521120704](https://s2.loli.net/2022/05/21/85EBJjDayMkXPfc.png)

### map和set
可看做一个定义好的类

### localStorage
可以在用户的浏览器上存储键值对。
一般刷新就消失了，要想让其不消失不用重新从服务器获取，就存到用户的浏览器里，类似cookie、用户偏好、浏览器缓存
```js
常用API：
localStorage.setItem(key, value)：插入
localStorage.getItem(key)：查找
localStorage.removeItem(key)：删除
localStorage.clear()：清空
```
<img src="https://s2.loli.net/2022/05/21/vwgO1YtNTsqEaLF.png" height=300px width=500px></img>

### JSON
JSON对象用于序列化对象、数组、数值、字符串、布尔值和null。因为很多函数(如websocket)的参数只能传字符串，需要把数组、map、函数之类的转化成字符串传进去，再解析成原来的类型
常用API：
```js
JSON.parse()：将字符串解析成对象
JSON.stringify()：将对象转化为字符串
```
![20220521122703](https://s2.loli.net/2022/05/21/L16Ujk4AYMrqePE.png)
### 日期
```js
返回值为整数的API，数值为1970-1-1 00:00:00 UTC（世界标准时间）到某个时刻所经过的毫秒数：

Date.now()：返回现在时刻。
Date.parse("2022-04-15T15:30:00.000+08:00")：返回北京时间2022年4月15日 15:30:00的时刻。
与Date对象的实例相关的API：
new Date()：返回现在时刻。
new Date("2022-04-15T15:30:00.000+08:00")：返回北京时间2022年4月15日 15:30:00的时刻。
两个Date对象实例的差值为毫秒数
getDay()：返回星期，0表示星期日，1-6表示星期一至星期六
getDate()：返回日，数值为1-31
getMonth()：返回月，数值为0-11
getFullYear()：返回年份
getHours()：返回小时
getMinutes()：返回分钟
getSeconds()：返回秒
getMilliseconds()：返回毫秒
```
### WebSocket
有些情况需要后端向前端发送请求，比如聊天室提醒有消息，http协议无法满足(但也可以用轮询的方法，如每隔10s问一下后端有没有信息)，于是有了websocket协议，两边都可主动发起通信
与服务器建立全双工连接。
常用API：
```js
new WebSocket('ws://localhost:8080');//建立ws连接。注意不是http协议而是ws协议 类似https有wss
send()：//向服务器端发送一个字符串。一般用JSON将传入的对象序列化为字符串。
onopen：//类似于onclick，当连接建立时触发。
onmessage：//当从服务器端接收到消息时触发。
close()：//关闭连接。
onclose：//当连接成功关闭后触发。
```

### window
```js
window.open("https://www.acwing.com")//在新标签栏中打开页面。
(window.)location.reload()//刷新页面。window可不写
(window.)location.href = "https://www.acwing.com"//在当前标签栏中打开页面。
```

### Canvas
可以使用js脚本在浏览器做动画或游戏
canvas的所有操作都是通过ctx(canvas[0].getContext('2d'))

# 五、中期项目：拳皇
动画基础：1秒24张图片
物体的移动
![20220521211820](https://s2.loli.net/2022/05/21/1mhxgQdNGZrPjpo.png)
templates放html
三个元素：地图和两个玩家，都要每秒刷新60次(game_object)
前端坐标系
![20220521215633](https://s2.loli.net/2022/05/21/yuC1MlqVEncIZYL.png)
聚焦才能让键盘输入字符，键盘的字符要输入的地方就是我们聚焦的地方(比如选择某个框输入文字)
如何判定角色能否攻击到对方：二维矩形，三维圆柱或球来代表元素
![20220521225145](https://s2.loli.net/2022/05/21/mvpJuf5akeV3jto.png)
要区分不同状态->状态机
![20220522000619](https://s2.loli.net/2022/05/22/e8FO46VvEdqcAky.png)
渲染gif的每一帧，容易控制速度
utils文件夹存辅助函数
![20220522005809](https://s2.loli.net/2022/05/22/gJH4c2Kz8Wru1XS.png)
注意多个函数里的this不再是类的this
偏移量可防止因为不同的图片人物到水平线以下
![20220522021346](https://s2.loli.net/2022/05/22/ypbE4CtvNueaFRZ.png)
![20220522023525](https://s2.loli.net/2022/05/22/xeYgDXQGIrz1ilS.png)
如何判定有没有攻击到对方：(碰撞检测)
两个图形是否有交集

一些不变的功能(如血条、计时器)不要在canvas里渲染，因为它1s会渲染60次，比较耗费资源

# 六、vue
## 文件目录
```
view是每个网站页面
router存的是跳转路由
components存组件
根组件是app.vue
入口在main.js
store就是vuex
```
每个.vue文件由三部分组成：html、js、css
css加scope会为当前页面的组件添加一个随机值，即特例化，不会影响到其他页面
## 渲染框架
后端渲染：每请求一个页面就向后端请求一次
前端渲染：第一次返回所有页面，样式存在一个js文件里
## 网站架构
![20220701213505](https://s2.loli.net/2022/07/01/TInvzKWVwRsYEmC.png)
## script部分
```js
export default对象的属性：
name：组件的名称
components：存储<template>中用到的所有组件
props：存储父组件传递给子组件的数据
watch()：当某个数据发生变化时触发
computed：动态计算某个数据
setup(props, context)：初始化变量、函数
ref定义变量，可以用.value属性重新赋值
reactive定义对象，不可重新赋值
props存储父组件传递过来的数据
context.emit()：触发父组件绑定的函数
```
引入bootstrap
```js
<script>
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap";
</script>
```
提示错误`Error: Can't resolve '@popperjs/core'`,需单独装下这个模块，直接在依赖里搜索
每个页面都需要用到NavBar组件=>在根组件里import(注意内容不能变)
## template部分
```html
<div class="container-fluid"></div>更偏左些，删去fluid则不靠边
bootstrap的card=>每个内容是一张卡片
bootstrap的container=>响应式地调整中间内容区域的大小
公共部分最好是用1个组件实现出来
<slot></slot>：存放父组件传过来的children。
v-on:click或@click属性：绑定事件
v-if、v-else、v-else-if属性：判断
v-for属性：循环，:key循环的每个元素需要有唯一的key
v-bind:或:：绑定属性
style部分
<style>标签添加scope属性后，不同组件间的css不会相互影响。
```
## style部分
```css
<style>标签添加scope属性后，不同组件间的css不会相互影响。
```
## router
```html
特殊属性:to (在vue里想给某个标签绑定属性要用冒号)
<router-link class="nav-link active" aria-current="page" :to="{name: 'home', params: {}}">首页</router-link>
name即为router里定义的name
```
## 页面布局
```
1.bootstrap的grid system 可分配每部分占的长宽
2.通过 Bootstrap 所提供的 .img-fluid 类让图片支持响应式布局。其原理是将 max-width: 100%; 和 height: auto; 赋予图片，以便随父元素的宽度变化一起缩放。
```
```
需要交互的数据存放到最顶层的组件里(如UserProfileView.vue),父子组件传递数值：父组件通过props，子组件通过event调用函数的方式实现
v-bind:user="user",不是一个普通的字符串，而是一个可传递的表达式
```
## 第三方组件
```html
view-router包：实现路由功能。<router-view />
vuex：存储全局状态，全局唯一。
state: 存储所有数据，可以用modules属性划分成若干模块
getters：根据state中的值计算新的值
mutations：所有对state的修改操作都需要定义在这里，不支持异步，可以通过$store.commit()触发
actions：定义对state的复杂修改操作，支持异步，可以通过$store.dispatch()触发。注意不能直接修改state，只能通过mutations修改state。
modules：定义state的子模块
```

---
# 总结

# 参考资料
1.[acwing](https://www.acwing.com/blog/)