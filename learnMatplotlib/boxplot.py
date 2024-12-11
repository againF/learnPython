import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
   'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Values': [7, 8, 6, 5, 6, 7]
})

sns.boxplot(data=data, x='Category', y='Values', palette='Set2')
plt.title('boxplot')
plt.show()