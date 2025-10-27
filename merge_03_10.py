import pandas as pd

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carlos"]
})

pedidos = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4],
    "valor": [100, 200, 300, 400]
})

df = pd.merge(clientes, pedidos, on="id_cliente", how="outer")
print(df)

df1 = pd.DataFrame({"nome": ["Ana", "Bruno", "Carlos"]}, index=[1, 2, 3])
df2 = pd.DataFrame({"idade": [25, 30, 22]})

df3 = df1.join(df2, how="inner")

print(df3)

# ----*
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df3)

# --
df1 = pd.DataFrame({"A": [1, 2, 3]})
df2 = pd.DataFrame({"B": ["x", "y", "z"]})

print(df1)
print(df3)
