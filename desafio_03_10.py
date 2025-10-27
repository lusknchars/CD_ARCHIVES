import pandas as pd

arquivo = pd.ExcelFile(
    "/Users/luskoliveira/Documents/DOCUMENTOS FUCAPE/ATIVIDADE_1B_CD/universidade_joins.xlsx")

alunos = pd.read_excel(arquivo, "alunos").set_index("cidade")
cidades = pd.read_excel(arquivo, "cidades").set_index("cidade")
disciplinas = pd.read_excel(arquivo, "disciplinas")
matriculas1 = pd.read_excel(arquivo, "matriculas_sem1")
matriculas2 = pd.read_excel(arquivo, "matriculas_sem2")

concat = pd.concat([matriculas1, matriculas2], axis=0, ignore_index=True)
print(concat)

merge_left = pd.merge(alunos, concat, on="matricula",
                      how="left", indicator=True)
print(merge_left)

alunos_cidades = alunos.join(cidades, how="left")
print(alunos_cidades)

cursos = pd.read_excel(arquivo, "alunos").set_index("curso")
print(cursos)

df = cursos

print(df.count())
