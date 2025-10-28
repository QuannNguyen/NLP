from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from src.models.text_classifier import TextClassifier


ds = load_dataset("zeroshot/twitter-financial-news-sentiment")

texts = ds["train"]["text"]
labels = ds["train"]["label"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42
)

# Train and evaluate
vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
classifier = TextClassifier(vectorizer)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

metrics = classifier.evaluate(y_test, y_pred)
for k, v in metrics.items():
    print(f"{k.capitalize()}: {v:.4f}")