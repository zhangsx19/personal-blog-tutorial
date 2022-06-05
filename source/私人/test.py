import base64


score = 25
print(base64.b64encode(str(score).encode('utf8')))