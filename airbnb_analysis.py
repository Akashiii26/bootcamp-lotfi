import pandas as pd

df = pd.read_csv("/Users/lotfimezzouar/Desktop/Bootcamp-lotfi/airbnb.csv")  # Assure-toi que le fichier CSV est dans le même dossier

print("Nombre total de lignes :", len(df))
print("Nombre de quartiers uniques :", df['neighbourhood'].nunique())
print("Top 5 quartiers :")
print(df['neighbourhood'].value_counts().head(5))
print("Prix moyen :", df['price'].mean())
