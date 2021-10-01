import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gorjetas = sns.load_dataset('tips')
gorjetas.head()

gorjetas.columns = ['custo_conta', 'gorjeta', 'sexo',
                    'fumante', 'dia', 'hora', 'tamanho-_grupo']
gorjetas.head()

plt.show()

fig, axes = plt.subplots()
axes.hist(gorjetas['custo_conta'])
axes.set_title('Histograma')
axes.set_xlabel('frequencia')
axes.set_ylabel('custo da conta')
fig.show()

plt.show()
