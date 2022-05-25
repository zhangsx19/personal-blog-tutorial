---
title: webCTF��¼
date: 2022-05-02 18:28:53
categories:
- CS
- security
tags:
- web
- CTF
toc: true
---
**ժҪ�����ļ�¼ˢ����web��**
<!-- more -->
---
# һ��xctf
## simple pHp
![20220516110337](https://s2.loli.net/2022/05/16/Wog1vasrdIbTc4C.png)
pHp tricks:
```
1.php���ַ��������ֱȽϴ�Сʱ����ʡ���ַ�
2.is_numeric ֻҪ���ַ����־���false
3.pHp�����ͱȽϣ�==����ɢ�Ƚϣ�ֻ�Ƚ�ֵ���Ƚ����ͣ�===���ϸ�Ƚϣ��Ƚ�ֵ������
```
```
php���������ֱȽϷ���:
�ַ��������ֱȽ�ʹ��==ʱ,�ַ�������ת��Ϊ���������ٱȽ�
var_dump('a' == 0);//true����ʱa�ַ�������ת�������֣���Ϊa�ַ���`��ͷ��û���ҵ�����`������ת��Ϊ0
var_dump('123a' == 123);//true������'123a'�ᱻת��Ϊ123
var_dump('a123' == 123);//false����Ϊphp��������һ���涨���ַ����Ŀ�ʼ���־���������ֵ��������ַ����ԺϷ������ֿ�ʼ����ʹ�ø��������������������һ�����ֽ�����������Ƚ�ʱ`����ֵΪ0`��
$a��aΪ�棬a����������0
```
��������urlΪ`http://111.198.29.45:44663/?a=a&b=1235a`

## get_post
![20220516112244](https://s2.loli.net/2022/05/16/wifBjbXr4GlOU13.png)
burpһ�������������(ע��a��Ϊget)
����content-lengthֻ��post�Ż��У�����Ҫ����ĳ�3

## xff_referer
X-Forwarder-For���ı䷢�������IP
Referer��Դ��ַ������ĿҪ���������https://www.google.com

## webshell
![20220516113037](https://s2.loli.net/2022/05/16/HDndGoLkfaWgZBT.png)
���ȴ���һ����Ϊshell�ı�����shell��ȡֵΪHTTP��POST��ʽ��Web��������shellȡֵ�Ժ�Ȼ��ͨ��eval()����ִ��shell��������ݡ�
���Խ����ϴ���д��webshell.php�ļ���Ȼ�����վ��Ŀ¼��ͨ����������ʣ���POST��ʽ����shell=phpinfo();
![20220516113627](https://s2.loli.net/2022/05/16/OXbxHpAwyZ2kr6D.png)
Ҳ�������Ͻ���˵��ȹ�������(�������õ����Ͻ�)����url��ַ��������http://127.0.0.1/webshell.php�������������������shell
![20220516113645](https://s2.loli.net/2022/05/16/haZTLzdnqNPltfs.png)
```
eval() �������ַ������� PHP ������ִ��
assert() ����ָ���� assertion ���ڽ��Ϊ FALSE ʱ��ȡ�ʵ����ж������ assertion ���ַ����������ᱻ assert() ���� PHP ������ִ�С�
```
[pHpһ�仰��](https://www.jianshu.com/p/6b815f951db3)

���ò˵�������
��burp����shell = system(��find / -name ��flag*����);
system("Linux����"),�൱�ڿ��˸�linux�ն�(/Ϊ��Ŀ¼��/home,/user)
�鿴 Response�����·���Ŀ���ļ�·��
shell = system(��cat /var/www/html/flag.txt��);
cat������linux�µ�һ���ı�������ͨ�������ڹۿ�ĳ���ļ������ݵ�

Ҳ����һ����ִ�ж��д��룺
```
shell=echo'<pre>';(echo��˫���ž���)Ч���ǳ��ָ�����
```
![20220516123133](https://s2.loli.net/2022/05/16/BHWQXlfEF8ikZoA.png)
grep �����ļ�������������ַ���

## ping
os����ִ��©��
![20220516124125](https://s2.loli.net/2022/05/16/Smflj7Ha3rV9egY.png)
����ʵ������������һ������Ĳ���
```
windows��linux������ִ��
command1 & command2 ������command1ִ�гɹ���񣬶���ִ��command2������һ������������Ϊ��һ����������룩��Ҳ����command1��command2��ִ��
command1 && command2 ����ִ��command1ִ�гɹ���Ż�ִ��command2����command1ִ��ʧ�ܣ���ִ��command2
command1 | command2 ��ִֻ��command2
command1 || command2 ��command1ִ��ʧ�ܣ���ִ��command2(��command1ִ�гɹ����Ͳ���ִ��command2)
```

## simple js
"\x49\x51\x5a\x56\x54"��C/C++ ����ͨ��ת���ַ���ֱ����cout ���� printf ������ʾ������
������55,56,54,79,115,69,114,116,107,49,50
var n = String.fromCharCode(65);//n = A ,�� Unicode ����תΪһ���ַ�
```
js�е����Ⱥ�˳��
��θ�ֵ��˳���޹أ���ͬʱ���и�ֵ��
ÿ���ڵ�ı������ո�ֵ��ֵȡ��ȥ���һ���Ⱥŵ��ұ�ֵ
�����ֵ���������ͣ�������ָ�����ͬһ������

JavaScript����Խ����ʲ��ᱨ��ֻ�᷵��undefined��
```
������Ʒ��ֽ��ֻ��pass�йأ������FAUX PASSWORD HAHA���������޹�
��һ����������ַ�����string����ˣ��뵽��pass����stringִ��һ��,p += chr(int(t2[17]))Ҫ����string�����һ��
exp���£�
![20220516233104](https://s2.loli.net/2022/05/16/uUWRPI6pnoi2re7.png)
## pHp2
![20220516174816](https://s2.loli.net/2022/05/16/cUuTyizS9jZWbrY.png)

ע�⣺������Ҫ��admin���ж��α���ſɳɹ�����Ϊ��������Զ�����һ��url���룬����֮�󴫵ݸ������൱��û���б��룬����admin

�����ȥ����һ�������������ҵ��ֵ���û��.phps��β�ģ���ɨ�����͹��ˡ�--����������ȡ�����ֵ�

```
.phps�ļ�����php��Դ�����ļ���ͨ�������ṩ���û��������ߣ��鿴php���룬��Ϊ�û��޷�ֱ��ͨ��Web���������php�ļ������ݣ�������Ҫ��phps�ļ����档��ʵ��ֻҪ����php���Ѿ��ڷ�������ע�����MIME����Ϊ�ļ����ɣ���Ϊ�˹���ͨ�ã����Բ�����phps�ļ����͡�
����MIME����Ϊ��text/html, application/x-httpd-php-source, application/x-httpd-php3-source
```
## ics-06
����id
intruder payload ѡnumber

## Web_php_unserialize
```
pHp��class
1��__construct()�������󴴽���new��ʱ���Զ����á����� unserialize() ʱ�ǲ����Զ����õġ������캯����
2��__destruct()������������ʱ���Զ����á�������������
3��__wakeup()��unserialize() ʱ���Զ�����
4.������ʽƥ��preg_match() ����
```
![20220517101903](https://s2.loli.net/2022/05/17/OesxJcE4dpGUDSg.png)
�������ǣ����flag��fl4g.php���ҳ���У����Demo�౻���٣���ô�ͻ������ʾfile��ָ����ļ������ݡ�
/[oc]:\d+:/i�о�
[OC]��������ʽ��o��c��ͷ
```
������ʽ�Ƕ��ַ���������һ���߼���ʽ�����������ȶ���õ�һЩ�ض��ַ�������Щ�ض��ַ�����ϣ����һ���������ַ�������
����������ַ��������������ַ�����һ�ֹ����߼���
\d:  ƥ��һ�������ַ����ȼ��� [0-9]��
 +:  ƥ��ǰ����ӱ��ʽһ�λ��Ρ����磬'zo+' ��ƥ�� "zo" �Լ� "zoo"��������ƥ�� "z"��+ �ȼ��� {1,}��
/i:  ��ʾƥ���ʱ�����ִ�Сд
```
__wakeup���ƹ�:
�����л��ַ����б�ʾ�������Ը�����ֵ������ʵ�����Ը���ʱ������__wakeup��ִ��,����ֻҪ��`O:4:��Demo��:1:{s:10:��Demofile��;s:8:��fl4g.php��;}`�е�1�Ǹĳ�����������������

# ����ctfhub
## 1.HTTP ���󷽷�
GET, POST �� HEAD������
OPTIONS, PUT, DELETE, TRACE �� CONNECT ����
```
OPTIONS
���ط���������ض���Դ��֧�ֵ�HTTP���󷽷���Ҳ����������web���������͡�*�������������Է������Ĺ�����
PUT
��ָ����Դλ���ϴ�����������
DELETE
���������ɾ��Request-URL����ʶ����Դ
TRACE
���Է������յ���������Ҫ���ڲ��Ի����
CONNECT
HTTP/1.1Э����Ԥ�����ܹ������Ӹ�Ϊ�ܵ���ʽ�Ĵ����������
```

## 2.HTTP��ʱ�ض���
����302��Ӧ�룬��ʱ��ת��location
ע��burpҪ�������ط�������Ӧ

## 3.������֤
������֤��Basic access authentication��������http�û������磺��ҳ�������������ʱ���ṩ �û��� �� ���� ��һ�ַ�ʽ
�ڽ��л�����֤�Ĺ���������HTTPͷ�ֶλ����Authorization�ֶΣ���ʽ���£� Authorization: Basic <ƾ֤>����ƾ֤���û����������͵�base64���롣��
```
GET /private/index.html HTTP/1.0
Host: localhost
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
```
ȱ�㣺������֤��û��Ϊ����ƾ֤��transmitted credentials���ṩ�κλ����Եı���������ʹ�� Base64 ���벢���䣬��û��ʹ���κ� ���� �� ɢ���㷨����ˣ�������֤������ HTTPS һ��ʹ�ã����ṩ�����ԡ�
���뱬�ƣ�Ҫȥ����Ч�غɱ���

## 4.xss
url����룺���Ƕ�֪��HttpЭ���в����Ĵ�����"key=value"���ּ�ֱ����ʽ�ģ����Ҫ�������������Ҫ�á�&�����ŶԼ�ֵ�Խ��зָ��"?name1=value1&name2=value2"�������ڷ�������յ������ַ�����ʱ�򣬻��á�&���ָ��ÿһ��������Ȼ�����á�=�����ָ������ֵ��
ȡ��valueʱ�����url����(hello���ܽ���ٴζ���hello)
send�൱�ڻ������Զ���������ύ����ַ
![20220521172751](https://s2.loli.net/2022/05/21/954LW8jHf1bKxdE.png)

# ����HackingLab ������Ϣ��ȫ����ѧϰƽ̨
## 1.�ű���
ͨ��`<script>window.location="./no_key_is_here_forever.php"; </script>`�ض�����
script��src ���Թ涨�ⲿ�ű��ļ��� URL��
## 2.XSS����3:����빹��
�鿴��Щ��ǩ�ؼ���û�б�����,����׼��һ��txt�ļ�ר�����ڼ��δ�����˺�����burp�Ϳ�������
![20220521184317](https://s2.loli.net/2022/05/21/5B6RYPh3Dba97Qq.png)
������Welcome <input type='text' value='123' onmouseover="eval(' ale'+'rt(HackingLab)')" s=''>
```
�����ͣ�����
�洢�ͣ����԰�
dom:�е�����
```
[xss�ƹ�](https://blog.csdn.net/nigo134/article/details/118827542)
