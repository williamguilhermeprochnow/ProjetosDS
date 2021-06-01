import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'resultado_dado1': np.random.randint(1, 7, 1_000_000),
    'resultado_dado2': np.random.randint(1, 7, 1_000_000)
}

df = pd.DataFrame(data)

df['soma_resultados'] = df.resultado_dado1 + df.resultado_dado2

print(df.head())

plt.hist(df.soma_resultados, bins=11)

plt.xlabel('Soma')
plt.ylabel('Quantidade de Lançamentos')
plt.title('Soma dos Resultados - Lançamento de Dados')

plt.tight_layout()
plt.show()

df.soma_resultados.value_counts()


###########################################################################


# data = {
#     'País': ['Belgica', 'India', 'Brasil', 'Somatória populacional'],
#     'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília', 'Total'],
#     'População': [123_465, 456_789, 987_654],
#     'Cor': ['red', 'orange', 'green', 'blue']
# }
#
# margem = [5, 2, 1, 1]
#
# soma = sum(data.get('População'))
# data.get('População').append(soma)
#
# for index, value in enumerate(data.get('País')):
#     plt.barh(str(data.get('População')[index]),
#              data.get('População')[index],
#              color=data.get('Cor')[index],
#              # xerr=margem[index],
#              label=data.get('País')[index] + ' - ' + data.get('Capital')[index])
#
#     plt.ylabel('População')
#     plt.xlabel('Escala 1/1000000')
#     plt.title('Gráfico demográfico')
#
#     plt.tight_layout()
#     plt.legend()
#
# plt.show()
