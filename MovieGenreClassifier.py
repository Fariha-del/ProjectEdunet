import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load data
data = pd.read_csv('movie_data.csv')

# Split data
X_train, X_test, y_train, y_test = train_test_split(data['PLOT'], data['GENRE'], test_size=0.2, random_state=42)

# Build model pipeline (TF-IDF + Naive Bayes)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train model
model.fit(X_train, y_train)

# Test model
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, 'movie_genre_model.joblib')
print("Model saved as movie_genre_model.joblib")
