
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Import trained components from backend
from ticket_ai import df, vectorizer, model


# ================= CATEGORY ACCURACY =================

# Features and labels
X = df["clean_document"]
y = df["Topic_group"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorize test data
X_test_vec = vectorizer.transform(X_test)

# Predict categories
y_pred = model.predict(X_test_vec)

# Calculate accuracy
category_accuracy = accuracy_score(y_test, y_pred)


# ================= DISPLAY RESULT =================

print("\n========== CATEGORY MODEL ACCURACY ==========\n")
print(f"Category Accuracy : {category_accuracy * 100:.2f}%")
