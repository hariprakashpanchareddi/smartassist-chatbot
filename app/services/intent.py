import spacy
from app.services.nlp import preprocess_text

nlp = spacy.load("en_core_web_sm")

# Define rule-based keyword sets (using lemmatized words where appropriate)
GREETINGS = {"hello", "hi", "hey", "greeting"}
COMPLAINTS = {"angry", "terrible", "bad", "awful", "suck", "complain", "complaint", "frustrated"}
ESCALATION = {"human", "agent", "manager", "supervisor", "representative", "person"}
TECHNICAL = {"api", "webhook", "ip", "browser", "sync", "export", "downtime", "integration", "bug", "error"}

def classify_intent(text: str) -> str:
    """
    Classifies the user's intent into: 'greeting', 'complaint', 'technical', 'escalation', or 'faq'.
    """
    doc = nlp(text.lower())
    raw_tokens = {token.text for token in doc}
    
    # 1. Check Greetings first (using raw tokens since words like 'hi' might be dropped by the preprocessor)
    if raw_tokens.intersection(GREETINGS):
        return "greeting"
        
    # 2. Use our custom NLP preprocessor (lemmatized, no stop words) for the rest
    processed = preprocess_text(text)
    lemmas = set(processed.split())
    
    if lemmas.intersection(ESCALATION):
        return "escalation"
        
    if lemmas.intersection(COMPLAINTS):
        return "complaint"
        
    if lemmas.intersection(TECHNICAL):
        return "technical"
        
    # Default to FAQ (RAG search) if no specific rules match
    return "faq"
