import simple_icd_10 as icd
import pandas as pd


def get_icd10_codes() -> pd.DataFrame:
    """
    Fetch all ICD-10-CM codes and their descriptions.

    Returns:
        pd.DataFrame: A DataFrame with 'Code' and 'Description' columns.
    """
    all_codes = icd.get_all_codes()
    data = [{"Code": code, "Description": icd.get_description(code)} for code in all_codes]
    return pd.DataFrame(data)


def export_icd10_to_excel(filepath: str = "icd10cm_codes.xlsx"):
    """
    Export all ICD-10-CM codes and their descriptions to an Excel file.

    Args:
        filepath (str): The path to the output Excel file.
    """
    df = get_icd10_codes()
    df.to_excel(filepath, index=False)
    print(f"ICD-10-CM codes exported to '{filepath}'")


if __name__ == "__main__":
    export_icd10_to_excel()
