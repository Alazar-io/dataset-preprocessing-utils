import pandas as pd

file_path = r"C:\Users\hp\Desktop\....\merged.csv"

df = pd.read_csv(file_path)

# Drop the 'id' column
df = df.drop(columns=['id']) # here change the column name into yours

# Save back to CSV
df.to_csv(file_path, index=False)

print("Column has been dropped!")