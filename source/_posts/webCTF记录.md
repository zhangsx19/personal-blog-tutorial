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

## pHp2
![20220516174816](https://s2.loli.net/2022/05/16/cUuTyizS9jZWbrY.png)

ע�⣺������Ҫ��admin���ж��α���ſɳɹ�����Ϊ��������Զ�����һ��url���룬����֮�󴫵ݸ������൱��û���б��룬����admin

�����ȥ����һ�������������ҵ��ֵ���û��.phps��β�ģ���ɨ�����͹��ˡ�--����������ȡ�����ֵ�

```
.phps�ļ�����php��Դ�����ļ���ͨ�������ṩ���û��������ߣ��鿴php���룬��Ϊ�û��޷�ֱ��ͨ��Web���������php�ļ������ݣ�������Ҫ��phps�ļ����档��ʵ��ֻҪ����php���Ѿ��ڷ�������ע�����MIME����Ϊ�ļ����ɣ���Ϊ�˹���ͨ�ã����Բ�����phps�ļ����͡�
����MIME����Ϊ��text/html, application/x-httpd-php-source, application/x-httpd-php3-source
```