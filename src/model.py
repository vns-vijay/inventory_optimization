from scipy.stats import norm

def newsvendor_optimal_order(price, cost, salvage, demand_mean, demand_std):
    critical_ratio = (price - cost) / (price - salvage)
    z = norm.ppf(critical_ratio)  # Inverse CDF of the standard normal distribution
    optimal_order = demand_mean + z * demand_std  # Convert to the actual demand scale
    return optimal_order
