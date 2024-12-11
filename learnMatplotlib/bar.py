import matplotlib.pyplot as plt

# 绘制柱状图

categories = ['A', 'B', 'C','D']
values = [25, 30, 15, 20]
plt.bar(categories, values,color="red")
plt.title("柱状图")
plt.xlabel("类别")
plt.ylabel("值")

plt.show()