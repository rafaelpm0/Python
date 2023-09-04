"""
Objetivo deste arquivo testes_pandas.py é sintetizar as estruturas de manipulação em pandas para ter um repositório
de consulta no futuro. Pq é coisa para uma p....

Aqui irá apenas constar o teste dos códigos, em anotações python, arquivo 29 contem todo detalhamento será e explica_
ções será posto lá.

O arquivo usado para teste será o tabela_pandas.csv

# CSV
import pandas as pd

# df = dataframe
df = pd.read_csv("tabela_pandas.csv", encoding="utf-8", sep=';')

df2 = pd.read_csv("tabela_pandas.csv", encoding="utf-8", sep=';', header=0, usecols= ['AddressID', 'AddressLine1',
                                                                                      'AddressLine2', 'City',
                                                                                      'StateProvinceID', 'PostalCode'])
df3 = pd.read_csv("tabela_pandas.csv", encoding="utf-8", sep=';', nrows=100)

print(df.shape)
print(list(df2))
print(df2)


# EXCEl

import  pandas as pd

df = pd.read_excel("tabela_pandas.xlsx", sheet_name=0)
print(str(df))

print(pd.ExcelFile("tabela_pandas.xlsx").sheet_names)
arquivo = pd.ExcelFile("tabela_pandas.xlsx")
print(arquivo.sheet_names)

arquivo = pd.ExcelFile("tabela_pandas.xlsx")
aba1 = arquivo.parse("tabela_pandas")
print(aba1)
print(aba1.head())


"""

