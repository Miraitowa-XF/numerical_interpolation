import numpy as np
import matplotlib.pyplot as plt

# 原始数据点
x_nodes = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
y_nodes = np.array([0.98, 0.92, 0.81, 0.64, 0.38])

# ------------------ 牛顿插值法 ------------------
def newton_interpolation(x_nodes, y_nodes, x):
    n = len(x_nodes)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y_nodes
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i+1][j-1] - diff_table[i][j-1]) / (x_nodes[i+j] - x_nodes[i])
    result = diff_table[0][0]
    product_term = 1.0
    for j in range(1, n):
        product_term *= (x - x_nodes[j-1])
        result += diff_table[0][j] * product_term
    return result

# ------------------ 自然三次样条插值 ------------------
def natural_cubic_spline(x_nodes, y_nodes, x):
    n = len(x_nodes) - 1  # 区间数
    h = np.diff(x_nodes)
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)
    
    # 自然边界条件
    A[0][0] = A[n][n] = 1
    
    # 填充三弯矩方程组
    for i in range(1, n):
        A[i][i-1] = h[i-1]
        A[i][i] = 2*(h[i-1] + h[i])
        A[i][i+1] = h[i]
        b[i] = 6 * ((y_nodes[i+1] - y_nodes[i])/h[i] - (y_nodes[i] - y_nodes[i-1])/h[i-1])
    
    # 求解 M
    M = np.linalg.solve(A, b)
    
    # 确定 x 所在区间
    for i in range(n):
        if x_nodes[i] <= x <= x_nodes[i+1]:
            dx = x - x_nodes[i]
            a = y_nodes[i]
            b = (y_nodes[i+1] - y_nodes[i])/h[i] - h[i]*(2*M[i] + M[i+1])/6
            c = M[i]/2
            d = (M[i+1] - M[i])/(6*h[i])
            return a + b*dx + c*dx**2 + d*dx**3
    return 0  # 超出范围返回0

# ------------------ 绘图 ------------------
x_plot = np.linspace(0.2, 1.0, 100)
y_newton = [newton_interpolation(x_nodes, y_nodes, x) for x in x_plot]
y_spline = [natural_cubic_spline(x_nodes, y_nodes, x) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.scatter(x_nodes, y_nodes, color='red', label='原始数据点')
plt.plot(x_plot, y_newton, 'b-', label='牛顿插值')
plt.plot(x_plot, y_spline, 'g--', label='三次样条')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('牛顿插值与三次样条插值对比')
plt.grid(True)
plt.show()