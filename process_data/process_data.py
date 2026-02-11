import pandas as pd
import glob

# Load all CSV files from data folder
files = glob.glob("data/*.csv")

df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsel
df = df[df["product"] == "pink morsel"]

# Clean price column (remove $ if present)
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Create Sales column
df["Sales"] = df["quantity"] * df["price"]

# Convert date column
df["Date"] = pd.to_datetime(df["date"])

# Keep only required columns
final_df = df[["Sales", "Date", "region"]]
final_df.rename(columns={"region": "Region"}, inplace=True)

# Save output file
final_df.to_csv("formatted_sales_data.csv", index=False)

print("Data processing complete! File saved as formatted_sales_data.csv")
