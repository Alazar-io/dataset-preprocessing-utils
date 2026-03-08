import pandas as pd

input_file = r" " 
output_file = r" " 

df = pd.read_csv(input_file)

# Mapping dictionary
label_map = {
    0: "neutral",
    1: "positive",
    2: "negative"
}

df["sentiment_en"] = df["sentiment"].map(label_map)

df.to_csv(output_file, index=False)

print("English sentiment column added!")