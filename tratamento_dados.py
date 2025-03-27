import pandas as pd
from pathlib import Path

pasta_script = Path(__file__).parent

arquivo1 = "EXP_2023_MUN.csv"
arquivo2 = "EXP_2024_MUN.csv"
arquivo_saida = "export_combined.csv"

df1 = pd.read_csv(pasta_script / arquivo1)
df2 = pd.read_csv(pasta_script / arquivo2)

pd.concat([df1, df2]).to_csv(pasta_script / arquivo_saida, index=False)

print(f"Arquivo combinado salvo em: {pasta_script / arquivo_saida}")
