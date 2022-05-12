import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import double
from scipy.interpolate import griddata
from matplotlib import cm

# 7/10

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

x1 = np.array(x01)
y1 = np.array(cof1)
x2 = np.array(x02)
y2 = np.array(cof2)
x3 = np.array(x03)
y3 = np.array(cof3)
x4 = np.array(x04)
y4 = np.array(cof4)
x5 = np.array(x05)
y5 = np.array(cof5)

z1 = np.polyfit(x1, y1, 3)              # 曲线拟合，返回值为多项式的各项系数
p1 = np.poly1d(z1)                    # 返回值为多项式的表达式，也就是函数式子
print(p1)
y_pred1 = p1(x1)                        # 根据函数的多项式表达式，求解 y
plt.grid(True, linestyle='--', alpha=0.9)
plot1 = plt.plot(x1, y1, '*', label='original values')
plo2 = plt.plot(x1, y_pred1, 'r', label='fit values')

z2 = np.polyfit(x2, y2, 3)            
p2 = np.poly1d(z2)                    
print(p2)
y_pred2 = p2(x2)                        
plt.grid(True, linestyle='--', alpha=0.9)
plot1 = plt.plot(x2, y2, '*', label='original values')
plo2 = plt.plot(x2, y_pred2, 'g', label='fit values')

z3 = np.polyfit(x3, y3, 3)            
p3 = np.poly1d(z3)                    
print(p3)
y_pred3 = p3(x3)                        
plt.grid(True, linestyle='--', alpha=0.9)
plot1 = plt.plot(x3, y3, '*', label='original values')
plo2 = plt.plot(x3, y_pred3, 'b', label='fit values')

z4 = np.polyfit(x4, y4, 3)            
p4 = np.poly1d(z4)                    
print(p4)
y_pred4 = p4(x4)                        
plt.grid(True, linestyle='--', alpha=0.9)
plot1 = plt.plot(x4, y4, '*', label='original values')
plo2 = plt.plot(x4, y_pred4, 'orange', label='fit values')

z5 = np.polyfit(x5, y5, 3)            
p5 = np.poly1d(z5)                    
print(p5)
y_pred5 = p5(x5)                        
plt.grid(True, linestyle='--', alpha=0.9)
plot1 = plt.plot(x5, y5, '*', label='original values')
plo2 = plt.plot(x5, y_pred5, 'black', label='fit values')


plt.title('The line graph of relationship between Coefficient of rolling friction and Initial velocity')
plt.xlabel('Initial velocity V0')
plt.ylabel('Coefficient of rolling friction')
plt.legend(loc=1, borderaxespad=0., bbox_to_anchor=(0, 0))
plt.legend(['0mT', '0mT', '50mT', '50mT', '100mT', '100mT', '150mT', '150mT', '200mT', '200mT'])  # 设置折线名称
plt.show()
print("Done.")
