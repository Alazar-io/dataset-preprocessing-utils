import pandas as pd

FILE = r"C:\Users\hp\Desktop\FInal_merged.csv"
output=r"C:\Users\hp\Desktop\CAC_DA_Sentiment_Dataset.csv"

df = pd.read_csv(FILE)

df["id"] = pd.to_numeric(df["id"], errors="coerce")

# Sort by ID ascending
df = df.sort_values("id")

df.to_csv(output, index=False, encoding="utf-8")

print("Dataset sorted by ID in ascending order")
