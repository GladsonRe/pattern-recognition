#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import random 
from sklearn.utils import shuffle


# In[ ]:


#Importa o arquivo com os dados como um dataset
arquivo = pd.read_csv('winedados.csv')


# In[ ]:


#Normalização estatistica dos dados: (X - Xmédia)/Xdesvio_padrão

def norm_estat(x):
    return ((x - x.mean())/x.std()) 

arquivo1 = arquivo.apply(norm_estat)
arquivo1 = arquivo1.drop('classe', axis=1)
arquivo1.insert(0,'classe',arquivo['classe'])


# In[ ]:


#converte o dataset em um array
arquivo2 =np.array(arquivo1)


# In[ ]:


#Embaralha o dataset
arquivo3 = shuffle(arquivo2)


# In[ ]:


#Separa o dataset em treino e teste na proporção 90/10
msk = np.random.rand(len(arquivo2)) <0.90
train = arquivo[msk]
test = arquivo[~msk]


# In[ ]:


train = shuffle(train)


# In[ ]:


treino = np.array(train)


# In[ ]:


teste = np.array(test)


# In[ ]:


len(treino)


# In[ ]:


len(teste)


# In[ ]:


norma = []
value1 = ''
value2 = ''
contador = 0
indice = 0
aux= 0


# In[ ]:


for j in range(len(teste)):
    for i in range(len(treino)):
        norma.append(np.linalg.norm(teste[j] - treino[i]))
        
    for i in range(len(norma)):
        if norma[i] == min(norma):
            indice = i


    for i in str(treino[indice]):
        if i == '.':
            break
        elif i == ' ':
            i = '0'
        else:
            value1 = value1 + i

    for i in str(teste[j]):
        if i == '.':
            break
        elif i == ' ':
            i = '0'
        else:
            value2 = value2 + i
            
    if value1 == value2:
        contador = contador + 1
    
    value1=''
    value2=''
    norma = []
    indice = 0
    
print("% Acerto",contador/len(teste)*100)
        

