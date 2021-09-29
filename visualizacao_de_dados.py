import matplotlib_inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib_inline

anscombe = sns.load_dataset('anscombe')
print(anscombe)

dataset_1 = anscombe[anscombe['dataset'] == 'I']
plt.plot(dataset_1.x, dataset_1.y)
plt.show()
