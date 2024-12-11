import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 2, 3, 4, 5],
    'category': ['A', 'B', 'A', 'B', 'A']
})

sns.scatterplot(data=data,x='x',y='y',hue='category',style='category',palette='deep')
plt.title('Scatterplot with hue and style')
plt.show()