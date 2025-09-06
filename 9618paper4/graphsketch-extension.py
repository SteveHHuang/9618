#implementing graph sketching using python
#source: 9231 w18 12

import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def y(x):
    return (5 * x**2 + 5 * x + 1) / (x**2 + x + 1)

# 生成x值范围（避免分母为零的点）
x = np.linspace(-10, 10, 1000)  # 从-10到10生成1000个点

# 计算对应的y值
y_values = y(x)

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(x, y_values, label=r'$y=\frac{5x^{2}+5x+1}{x^{2}+x+1}$', color='blue')
plt.title('Graph of the Function $y = \\frac{5x^{2}+5x+1}{x^{2}+x+1}$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axhline(y=5, color='red', linestyle='--', label='Horizontal Asymptote y=5')  # 水平渐近线
plt.axvline(x=0, color='green', linestyle=':', alpha=0.5)  # y轴参考线
plt.axhline(y=0, color='green', linestyle=':', alpha=0.5)  # x轴参考线
plt.legend()
plt.show()

