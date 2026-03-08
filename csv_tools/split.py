import pandas as pd
import numpy as np

# Path to the file
merged_file = r"C:\Users\hp\Desktop\final_final.csv"

# Read the merged dataset 
df = pd.read_csv(merged_file, sep='\t', names=['id', 'amharic'], encoding='utf-8')

# Number of parts
n_parts = 13

# Calculate roughly equal sizes
total_rows = len(df)
part_size = total_rows // n_parts  

# Split and save
for i in range(n_parts):
    start_idx = i * part_size
    if i == n_parts - 1:
        end_idx = total_rows
    else:
        end_idx = (i + 1) * part_size

    df_part = df.iloc[start_idx:end_idx]
    df_part.to_csv(f"part_{i+1}.txt", sep='\t', index=False, header=False, encoding='utf-8')

print(f"Merged file split into {n_parts} parts successfully!")
