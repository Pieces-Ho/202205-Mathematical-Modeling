import os

from numpy import double

x01 = []
x02 = []
x03 = []
x04 = []
x05 = []
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
cof1 = []
cof2 = []
cof3 = []
cof4 = []
cof5 = []

file_path = 'C:\\Users\\MZ Huo\\Desktop\\model.txt'
with open(file_path, encoding='utf-8') as file_obj:

    lines = file_obj.readlines()
    for l in lines:
        st = l.rstrip()
        a,b, c,d, e,f, g,h, m,n = (map(double ,st.split()))
        x01.append(a)
        v1.append(b)
        x02.append(c)
        v2.append(d)
        x03.append(e)
        v3.append(f)
        x04.append(g)
        v4.append(h)
        x05.append(m)
        v5.append(n)
        
        
# for k in range(len(v1)):
#     print("x1:",x01[k],",v1:",v1[k], ",x2:",x02[k],",v2:",v2[k], ",x3:",x03[k],",v3:",v3[k], ",x4:",x04[k],",v4:",v4[k],",x5:",x05[k],",v5:",v5[k], end = "\n")

for k in range(len(v1)):
    tp1 = ((x01[k]**2-v1[k]**2)*0.07)/9.80665
    cof1.append(tp1)
    tp2 = ((x02[k]**2-v2[k]**2)*0.07)/9.80665
    cof2.append(tp2)
    tp3 = ((x03[k]**2-v3[k]**2)*0.07)/9.80665
    cof3.append(tp3)
    tp4 = ((x04[k]**2-v4[k]**2)*0.07)/9.80665
    cof4.append(tp4)
    tp5 = ((x05[k]**2-v5[k]**2)*0.07)/9.80665
    cof5.append(tp5)
    
for s in range(len(v1)):
    print("c1: ",cof1[s],",c2: ",cof2[s],",c2: ",cof3[s],",c4: ",cof4[s],",c5: ",cof5[s])