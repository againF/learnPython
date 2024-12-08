# 模拟学生的成绩分布，计算其均值、方差，并绘制分布图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 模拟 100 个学生的成绩（正态分布）
scores = np.random.normal(75, 10, 100)

# 创建一个 DataFrame
df = pd.DataFrame(scores, columns=['Score'])

# 计算均值和方差标准差
mean = df['Score'].mean()
variance = df['Score'].var()
std_deviation = df['Score'].std()

print('均值Mean:', mean)
print('方差Variance:', variance)
print('标准差Standard Deviation:', std_deviation)

# 绘制成绩分布图
plt.hist(df['Score'], bins=20,edgecolor='black')
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()