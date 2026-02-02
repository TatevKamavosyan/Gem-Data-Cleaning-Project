import pandas as pd

df = pd.read_csv(r'Gem_data_clean_export.csv', sep=";", engine='python')
print(df.columns.tolist())

df.columns = df.columns.str.strip()

df_final = df[['GemName', "Usage(GS)", "%Usage", "Usage(NR)", "Downloads"]].dropna().copy()


# 2. Rounding without changing decimal point
df_final = df_final.round(4)

# 3. Save
file_name = "Gem_data_cleaned.csv"
df_final.to_csv(file_name, index=False, encoding="utf-8-sig", quoting=0)



print("First 5 rows of processed data:")
print(df_final.head(9))


