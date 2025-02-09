import numpy as np
import pandas as pd
from src.model import newsvendor_optimal_order
from src.gendata import generate_data


num_products = 5

# Random data generation
df = generate_data(num_products)


df["Optimal_Order"] = df.apply(
    lambda row: newsvendor_optimal_order(row["Price"], row["Cost"], row["Salvage"], row["Demand_Mean"], row["Demand_Std"]),
    axis=1
)

df["Optimal_Order"] = df["Optimal_Order"].round().astype(int)


df.to_csv("data/newsvendor_data.csv", index=False)


print(df)


