from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# 加载数据
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names
# 数据拆分：训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 模型训练：决策树分类器
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# 可视化决策树
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=feature_names, class_names=class_names, filled=True)
plt.show()
# 模型预测
y_pred = model.predict(X_test)
# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"分类准确率：{accuracy:.2f}")

accuracy2 = model.score(X_test, y_test)
print(f"模型准确率：{accuracy2:.2f}")