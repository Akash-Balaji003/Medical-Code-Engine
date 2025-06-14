import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS
from medical_abbreviations import medical_abbreviations

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_diagnosis(text: str) -> str:
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Expand abbreviations
    words = text.split()
    expanded_words = [
        medical_abbreviations.get(word.strip(string.punctuation), word)
        for word in words
    ]
    expanded_text = " ".join(expanded_words)

    # Step 3: Process with SpaCy
    doc = nlp(expanded_text)

    # Step 4: Remove stopwords, punctuation, and lemmatize
    tokens = [
        token.lemma_
        for token in doc
        if token.text not in STOP_WORDS and token.text not in string.punctuation
    ]

    # Step 5: Return clean string
    return " ".join(tokens)


if __name__ == "__main__":
    while True:
        raw_input_text = input("\nEnter medical diagnosis (or type 'exit' to quit):\n> ")
        if raw_input_text.lower() == "exit":
            print("Exiting.")
            break

        cleaned_output = preprocess_diagnosis(raw_input_text)
        print("\n🧹 Processed diagnosis:\n", cleaned_output)
