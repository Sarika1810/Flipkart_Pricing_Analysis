import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
# required column
df = df[["category_1", "selling_price", "mrp", "product_rating"]]

#rename
df.rename(columns={
    "category_1":"category",
    "selling_price":"discounted_price",
    "mrp":"original_price",
    "product_rating":"rating"
}, inplace=True)

df["discounted_price"] = (
    df["discounted_price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["original_price"] = (
    df["original_price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["discount_pct"] = (
    (df["original_price"] - df["discounted_price"])
    / df["original_price"]
) * 100




df["price_ending"] = df["discounted_price"] % 100

df["pricing_type"] = df["price_ending"].apply(
    lambda x: "Charm" if x == 99 else "Round" if x == 0 else "Other"
)



#numpy

np.random.seed(10)

df["units_sold"] = np.random.randint(50, 500, len(df))

print(df.head())

df.to_csv("pricing_analysis.csv", index=False)

print("File Saved Successfully")
