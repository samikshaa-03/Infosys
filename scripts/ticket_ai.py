# ===================== STEP 1: IMPORT LIBRARIES =====================
import re
import os
import uuid
from datetime import datetime
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# ===================== STEP 2: LOAD spaCy MODEL =====================
nlp = spacy.load("en_core_web_sm")


# ===================== STEP 3: LOAD DATASET (PATH SAFE) =====================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "all_tickets_processed_improved_v3.csv")

df = pd.read_csv(DATA_PATH)
print("✅ Dataset loaded successfully")


# ===================== STEP 4: FIX DATASET INCONSENCIES =====================
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["Document"] = df["Document"].astype(str).str.strip()
df["Topic_group"] = df["Topic_group"].astype(str).str.strip()


# ===================== STEP 5: TEXT CLEANING FUNCTION =====================
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ===================== STEP 6: APPLY PREPROCESSING =====================
df["clean_document"] = df["Document"].apply(clean_text)


# ===================== STEP 7: DEFINE FEATURES & LABELS =====================
X = df["clean_document"]
y = df["Topic_group"]


# ===================== STEP 8: TF-IDF VECTORISATION =====================
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)


# ===================== STEP 9: TRAIN CATEGORY MODEL =====================
model = MultinomialNB()
model.fit(X_vec, y)
print("✅ Ticket category model trained successfully")


# ===================== STEP 10: INPUT VALIDATION =====================
def is_valid_ticket(text):
    greetings = [
        "hi", "hello", "hey", "how are you",
        "thanks", "ok", "okay", "yes", "no"
    ]

    cleaned = clean_text(text)
    words = cleaned.split()

    # Very short input
    if len(words) <= 3:
        return False

    # Greeting-only input
    if cleaned in greetings:
        return False

    return True


# ===================== STEP 11: ERROR CODE EXTRACTION =====================
def extract_error_codes(text):
    return re.findall(r"\b\d{3,4}\b", text)


# ===================== STEP 12: ENTITY EXTRACTION =====================
def extract_entities(text):
    devices = []

    device_keywords = [
        "laptop", "mouse", "keyboard", "printer",
        "wifi", "router", "monitor", "cpu"
    ]

    for token in text.lower().split():
        if token in device_keywords:
            devices.append(token)

    return {
        "devices": list(set(devices)),
        "error_codes": extract_error_codes(text)
    }


# ===================== STEP 13: CATEGORY PREDICTION =====================
def predict_category(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    return str(model.predict(vec)[0])


# ===================== STEP 14: TICKET GENERATION ENGINE =====================
def generate_ticket(user_input):

    # 🔴 INPUT VALIDATION CHECK
    if not is_valid_ticket(user_input):
        return {
            "status": "invalid",
            "message": "Input is not a valid support ticket. Please describe a real issue."
        }

    cleaned_description = clean_text(user_input)
    category = predict_category(user_input)
    entities = extract_entities(user_input)

    # Priority logic
    urgent_keywords = ["urgent", "asap", "immediately", "not working", "down"]
    if any(word in user_input.lower() for word in urgent_keywords):
        priority = "High"
    else:
        priority = "Low"

    ticket = {
        "ticket_id": uuid.uuid4().hex[:8],
        "title": f"{category.capitalize()} Issue",
        "description": user_input,
        "cleaned_description": cleaned_description,
        "category": category,
        "priority": priority,
        "entities": entities,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }

    return ticket


# ===================== BACKEND TEST =====================
if __name__ == "__main__":
    test_inputs = [
        "hi",
        "how are you",
        "mouse not working",
        "server is down urgently"
    ]

    for text in test_inputs:
        print("\nINPUT:", text)
        output = generate_ticket(text)
        for k, v in output.items():
            print(f"{k}: {v}")
