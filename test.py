
# Alt + Shift + A ： 快速注释多行代码
# Ctrl + / ： 快速注释一行代码

""" from matplotlib import pyplot as plt
import numpy as np
#创建图形对象和轴域对象
fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
#绘制直方图
ax.hist(a, bins = [0,25,50,75,100,125,150])
#设置坐标轴
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100,125,150])
ax.set_xlabel('marks')
ax.set_ylabel('no.of students')
plt.show() """

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
  x = np.arange(1, 31, 1)
  y = np.array([20, 23, 26, 29, 32, 35, 38, 45, 53, 62, 73, 86, 101, 118, 138, 161, 188, 220, 257, 300, 350, 409, 478, 558, 651, 760, 887, 1035, 1208, 1410])

  z1 = np.polyfit(x, y, 3)              # 曲线拟合，返回值为多项式的各项系数
  p1 = np.poly1d(z1)                    # 返回值为多项式的表达式，也就是函数式子
  print(p1)
  y_pred = p1(x)                        # 根据函数的多项式表达式，求解 y
  #print(np.polyval(p1, 29))             #根据多项式求解特定 x 对应的 y 值
  #print(np.polyval(z1, 29))             #根据多项式求解特定 x 对应的 y 值
  plot1 = plt.plot(x, y, '*', label='original values')
  plot2 = plt.plot(x, y_pred, 'r', label='fit values')
  plt.title('')
  plt.xlabel('')
  plt.ylabel('')
  plt.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0))
  plt.show()



print("OK py.")

