import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib_inline

anscombe = sns.load_dataset('anscombe')
#print(anscombe)

dataset_1 = anscombe[anscombe['dataset'] == 'I']
plt.plot(dataset_1.x, dataset_1.y)
#plt.show()

dataset_2 = anscombe[anscombe['dataset']=='II']
dataset_3 = anscombe[anscombe['dataset']=='III']
dataset_4 = anscombe[anscombe['dataset']=='IV']

plt.plot(dataset_1.x, dataset_1.y, 'o')
#plt.show()

fig, axes = plt.subplots(ncols=2,nrows=2, figsize=(15,10))

plt.show()

axes[0,0].plot(dataset_1.x,dataset_1.y,'o')
axes[0,1].plot(dataset_2.x,dataset_2.y,'o')
axes[1,0].plot(dataset_3.x,dataset_3.y,'o')
axes[1,1].plot(dataset_4.x,dataset_4.y,'o')

plt.show()