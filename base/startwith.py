import re
p = ["G1212","F232",'M2323','YSF23232','YSM34343']

for i in p:
    print(i.startswith(('F','M','YSF','YSM')))
    print(True if re.match('F|M|YSF|YSM', i) else False)