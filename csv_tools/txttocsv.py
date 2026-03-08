import os
import pandas as pd

folder = r"" # here enter the path to your txt file

for file in os.listdir(folder):
    if file.endswith(".txt"):
        txt_path = os.path.join(folder, file)

        df = pd.read_csv(txt_path, sep=",", engine="python")

        csv_name = file.replace(".txt", ".csv")
        csv_path = os.path.join(folder, csv_name)

        df.to_csv(csv_path, index=False)

print("All txt files converted to CSV!")