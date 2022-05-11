import matplotlib.pyplot as plt
import numpy as np
from numpy import double

if __name__ == "__main__":
    v0 = []
    v1 = []
    cof = []
    file_path = 'C:\\Users\\MZ Huo\\Desktop\\200mt.txt'
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

    x = np.array(v0)
    y = np.array(cof)

    z1 = np.polyfit(x, y, 3)              # 曲线拟合，返回值为多项式的各项系数
    p1 = np.poly1d(z1)                    # 返回值为多项式的表达式，也就是函数式子
    print(p1)
    y_pred = p1(x)                        # 根据函数的多项式表达式，求解 y
 
    plot1 = plt.plot(x, y, '*', label='original values')
    plot2 = plt.plot(x, y_pred, 'r', label='fit values')
    plt.title('The line graph of relationship between Coefficient of rolling friction and Initial velocity when 0mT')
    plt.xlabel('Initial velocity V0')
    plt.ylabel('Coefficient of rolling friction')
    plt.legend(loc=1, borderaxespad=0., bbox_to_anchor=(0, 0))
    plt.show()