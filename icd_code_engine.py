import pandas as pd
from sentence_transformers import SentenceTransformer, util


def load_icd_data(filepath: str) -> pd.DataFrame:
    """Load ICD-10 code data from a CSV file and return a cleaned DataFrame."""
    df = pd.read_csv(filepath)
    df = df[['Code', 'Description']].dropna()
    return df


def find_icd_matches(diagnosis: str, df: pd.DataFrame, model: SentenceTransformer, top_n: int = 5):
    """
    Find top ICD-10 code matches for a given diagnosis using semantic similarity.

    Args:
        diagnosis (str): Free-text diagnosis description.
        df (pd.DataFrame): DataFrame with 'Code' and 'Description'.
        model (SentenceTransformer): Pre-trained sentence transformer model.
        top_n (int): Number of top matches to return.

    Returns:
        pd.DataFrame: Top N matched ICD codes with similarity scores.
    """
    descriptions = df['Description'].tolist()

    embedding_diagnosis = model.encode(diagnosis, convert_to_tensor=True)
    embedding_descriptions = model.encode(descriptions, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embedding_diagnosis, embedding_descriptions)[0]
    df['score'] = cosine_scores.cpu().numpy()

    top_matches = df.sort_values(by='score', ascending=False).head(top_n)
    return top_matches


def main():
    print("Initializing ICD-10 Code Matcher...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    icd_df = load_icd_data('ICD-10_Codes/icd10_codes.csv')
    
    # Example diagnosis input
    diagnosis = "Patient has hypertension"
    print("Diagnosis:", diagnosis)

    matches = find_icd_matches(diagnosis, icd_df, model)

    print("\nTop ICD-10 Matches:\n")
    for _, row in matches.iterrows():
        print(f"{row['Code']} - {row['Description']}  →  Score: {row['score']:.4f}")


if __name__ == "__main__":
    main()
