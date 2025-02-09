import numpy as np
import pandas as pd




def generate_data(num_products=5):
    np.random.seed(42) 

    data = {
        "Product": [f"Product_{i+1}" for i in range(num_products)],
        "Price": np.random.uniform(50, 100, num_products).round(2),  # Selling price
        "Cost": np.random.uniform(20, 40, num_products).round(2),    # Purchase cost
        "Salvage": np.random.uniform(5, 15, num_products).round(2),  # Salvage value
        "Demand_Mean": np.random.randint(100, 200, num_products),    # Mean demand
        "Demand_Std": np.random.randint(10, 30, num_products)        # Demand standard deviation
    }

    df = pd.DataFrame(data)

    return df
