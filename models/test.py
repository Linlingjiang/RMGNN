import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
# k2 和 k1 的不同组合值
k2 = [0.01, 0.05, 0.5]
k1 = [0.01, 0.05, 0.5]

# 创建一个 3x3 的准确率数据矩阵
data = np.array([
    [66.9, 66.6, 66.9],
    [66.2, 67.2, 67.5],
    [66.6, 67.7, 67.4]
])

# 创建热力图
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, fmt='.1f', cmap='coolwarm', xticklabels=k2, yticklabels=k1)

# 设置标题和标签
plt.title('Accuracy of RMGNN with Different k1 and k2 Values')
plt.xlabel('k2')
plt.ylabel('k1')

# 显示图形
plt.show()
