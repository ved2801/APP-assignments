import numpy as np

def analyze_rainfall():
    # Rainfall data (in mm) for 12 months (January to December)
    rainfall = np.array([45.5, 30.2, 25.0, 60.5, 110.0, 250.4, 280.2, 210.0, 95.5, 70.0, 40.0, 35.0])
    months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # 1) Compute total and average annual rainfall
    total_rainfall = np.sum(rainfall)
    average_rainfall = np.mean(rainfall)
    
    print("--- Annual Rainfall Summary ---")
    print(f"Total Annual Rainfall: {total_rainfall:.2f} mm")
    print(f"Average Monthly Rainfall: {average_rainfall:.2f} mm\n")
    
    # 2) Identify months with rainfall above 100 mm using logical indexing
    above_100_mask = rainfall > 100
    heavy_months = months[above_100_mask]
    heavy_values = rainfall[above_100_mask]
    
    print("--- Months with Rainfall > 100 mm ---")
    for month, val in zip(heavy_months, heavy_values):
        print(f"{month}: {val} mm")

if __name__ == "__main__":
    analyze_rainfall()
