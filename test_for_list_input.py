import os

from numpy import double

v0 = []
v1 = []
cof = []
file_path = 'C:\\Users\\MZ Huo\\Desktop\\0mt.txt'
with open(file_path, encoding='utf-8') as file_obj:

    lines = file_obj.readlines()
    for l in lines:
        st = l.rstrip()
        a, b = (map(double ,st.split()))
        v0.append(a)
        v1.append(b)
        
        

for k in range(len(v0)):
    tp = ((v0[k]**2-v1[k]**2)*0.07)/9.80665
    cof.append(tp)
    print("v0: ",v0[k], end = "  ")    
    print("v1: ",v1[k])  
    
for s in cof:
    print(s) 
