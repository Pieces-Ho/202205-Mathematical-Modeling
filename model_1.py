import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

  aa = [0.249845,0.256786,0.264122]

  x = np.array(aa)
  y = np.array([0.000257826, 0.000234386, 0.000267373])

  z1 = np.polyfit(x, y, 3)              # 曲线拟合，返回值为多项式的各项系数
  p1 = np.poly1d(z1)                    # 返回值为多项式的表达式，也就是函数式子
  print(p1)
  y_pred = p1(x)                        # 根据函数的多项式表达式，求解 y
 
  plot1 = plt.plot(x, y, '*', label='original values')
  plot2 = plt.plot(x, y_pred, 'r', label='fit values')
  plt.title('TITLE')
  plt.xlabel('X-axis')
  plt.ylabel('Y-axis')
  plt.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0))
  plt.show()