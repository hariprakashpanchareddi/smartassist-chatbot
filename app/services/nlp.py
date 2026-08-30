import spacy

# Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    """
    Preprocesses input text by tokenizing, lemmatizing, 
    and removing stop words, spaces, and punctuation.
    """
    doc = nlp(text)
    
    # Extract the base form (lemma) of words that aren't stop words or punctuation
    tokens = [
        token.lemma_.lower() 
        for token in doc 
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    
    return " ".join(tokens)
