import pandas as pd
import glob
import os

path = r"C:\Users\hp\Desktop\merged quad"
all_files = sorted(glob.glob(os.path.join(path, "*.csv")))

dfs = []

for file in all_files:
    df = pd.read_csv(file,  on_bad_lines='skip', engine='python')
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv(r"C:\Users\hp\Desktop\merged quad\merged.csv", index=False)
print("All files merged successfully!")