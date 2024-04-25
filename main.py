import pandas as pd

# Read the CSV file
data = pd.read_csv("Australia Address.csv")

# Extract unique combinations of street name, suburb, and region
unique_addresses = data.drop_duplicates(subset=["street", "suburb", "region"])

# Select desired columns
unique_addresses = unique_addresses[["street", "suburb", "region", "postcode"]]

# Remove ".0" from postcodes
unique_addresses["postcode"] = unique_addresses["postcode"].astype(int)

# Save the unique addresses to a new CSV file
unique_addresses.to_csv("output.csv", index=False)
