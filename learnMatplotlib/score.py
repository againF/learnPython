import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)
scores = {
    'Math': np.random.normal(70,10,100),
    'Science': np.random.normal(75,12,100),
    'English': np.random.normal(80,8,100),
}
df = pd.DataFrame(scores)
print(df.describe())

sns.histplot(df, kde=True,element="step",palette='muted')
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

