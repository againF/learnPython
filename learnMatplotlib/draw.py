import matplotlib.pyplot as plt

x = [1, 2, 3, 4,5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y,label='y = 2x',color="red",marker="o")
plt.title("折线图")
plt.xlabel("x轴")

plt.ylabel("y轴")
plt.legend()
# plt.show()

categories = ['A', 'B', 'C','D']
values = [25, 30, 15, 20]
plt.bar(categories, values,color="red")
plt.title("柱状图")
plt.xlabel("类别")
plt.ylabel("值")

plt.show()