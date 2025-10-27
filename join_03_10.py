import pandas as pd

arquivo = pd.ExcelFile("aula_pandas_joins.xlsx")
clientes = pd.read_excel(arquivo, "clientes")
pedidos = pd.read_excel(arquivo, "pedidos")
pop = pd.read_excel(arquivo, "populacao")
area = pd.read_excel(arquivo, "area")
jan = pd.read_excel(arquivo, "vendas_jan")
fev = pd.read_excel(arquivo, "vendas_fev")
mar = pd.read_excel(arquivo, "vendas_mar")

merge = pd.merge(clientes, pedidos, on="id_cliente", how="left")
print(merge)


concat = pd.concat([jan, fev, mar], axis=0, ignore_index=True)
print(concat)
