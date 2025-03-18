import pandas as pd
import os

# Define file paths (update the folder path)
folder_path = "AccessGUDID_Delimited_Full_Release_20250207"

# Load each file into a DataFrame
# device_df = pd.read_csv(f"{folder_path}/device.txt",
#     delimiter="|",  # Use "|" as separator
#     dtype=str,      # Read all columns as strings
#     encoding="utf-8",
#     on_bad_lines="skip")
files = ["device.txt", "contacts.txt", "deviceSizes.txt", "environmentalConditions.txt", "gmdnTerms.txt", "identifiers.txt", "premarketSubmissions.txt", "productCodes.txt", "sterilizationMethodTypes.txt"]
dfs = {}

# for f in files[:3]:
#     filename = f[:-4]
#     dfs[filename] = pd.read_csv(os.path.join(folder_path, f), delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")

# result_df = dfs["device"]

# for dfname, df in dfs.items():
#     if dfname != "device":
#         result_df = pd.merge(result_df, df, on="PrimaryDI", how='left')

# print(result_df.head())


# Read all files into DataFrames
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path, delimiter="|", dtype=str)  # Assuming "|" as the delimiter
        dfs[file] = df  # Store DataFrame in dictionary
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Get the main DataFrame to start merging
merged_df = dfs["device.txt"]  # Start with the device.txt DataFrame

# Merge all other DataFrames on 'PrimaryDI'
for file, df in dfs.items():
    if file != "device.txt":  # Skip the first one since it's already in merged_df
        merged_df = merged_df.merge(df, on="PrimaryDI", how="left")  # Left join

# Save merged dataset to CSV
merged_df.to_csv("merged_dataset.csv", index=False)

print("✅ Merging complete! Data saved as 'merged_dataset.csv'.")
print(merged_df.head()) 
    




# for file in files:
#     file_path = os.path.join(folder_path, file)
#     try:
#         df = pd.read_csv(file_path, delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")  # Assuming "|" as the delimiter
#         print(f"\n===== {file} =====")
#         print(df.head())  # Print first 5 rows
#     except Exception as e:
#         print(f"Error reading {file}: {e}")
# contacts_df = pd.read_csv(f"{folder_path}/contacts.txt", delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")
# devicesize_df = pd.read_csv(f"{folder_path}/deviceSizes.txt", delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")
# identifier_df = pd.read_csv(f"{folder_path}/identifiers.txt", delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")
# productcode_df = pd.read_csv(f"{folder_path}/productCodes.txt", delimiter="|", dtype=str, encoding="utf-8", on_bad_lines="skip")

# print(device_df.head())