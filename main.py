import simple_icd_10 as icd
import pandas as pd

# Initialize the ICD-10 codes to store in the database
all_codes = icd.get_all_codes()

# Prepare a list of dicts with code and description
data = [{"Code": code, "Description": icd.get_description(code)} for code in all_codes]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("icd10cm_codes.xlsx", index=False)

print("ICD-10-CM codes exported to 'icd10cm_codes.xlsx'")
