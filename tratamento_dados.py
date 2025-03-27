import pandas as pd

df1 = pd.read_csv("C:/Users/malen/Desktop/API 2025/EXP_2023_MUN.csv")
df2 = pd.read_csv("C:/Users/malen/Desktop/API 2025/EXP_2024_MUN.csv")
combined = pd.concat([df1, df2])

caminho_saida = "C:/Users/malen/Desktop/API 2025/export_combined.csv"
combined.to_csv(caminho_saida, index=False)