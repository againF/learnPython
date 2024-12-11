import matplotlib.pyplot as plt
# 创建数据
x = [1, 2, 3, 4,5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y,label='y = 2x',color="red",marker="o")
plt.title("折线图")
plt.xlabel("x轴")

plt.ylabel("y轴")
plt.legend()
plt.show()

