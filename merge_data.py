import pandas as pd
import os

folder_path = "AccessGUDID_Delimited_Full_Release_20250207"

files = ["device.txt", "contacts.txt", "deviceSizes.txt", "environmentalConditions.txt", "gmdnTerms.txt", "identifiers.txt", "premarketSubmissions.txt", "productCodes.txt", "sterilizationMethodTypes.txt"]
dfs = {}


# Read files
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path, delimiter="|", dtype=str)  
        dfs[file] = df  
    except Exception as e:
        print(f"Error reading {file}: {e}")


merged_df = dfs["device.txt"]  

# PrimaryDI
for file, df in dfs.items():
    if file != "device.txt":  
        merged_df = merged_df.merge(df, on="PrimaryDI", how="left")  n


merged_df.to_csv("merged_dataset.csv", index=False)

print("Saved as 'merged_dataset.csv'.")
print(merged_df.head()) 
    