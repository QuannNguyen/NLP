## Implementation Steps

### Step 1 — Dataset Loading
- Used the **Hugging Face** dataset `zeroshot/twitter-financial-news-sentiment`.  
- Dataset contains financial tweets labeled as `negative`, `neutral`, or `positive`.  
- Used the `"train"` split for both training and evaluation (split 80/20 manually).

### Step 2 — Text Vectorization
- Applied **TF–IDF vectorization** using `TfidfVectorizer` from scikit-learn.  
- Limited vocabulary to **5000 features** and removed English stopwords to reduce noise.  
- This converts raw text into numerical vectors suitable for machine learning.

### Step 3 — Model Implementation
- Implemented a `TextClassifier` class in `src/models/text_classifier.py`.  
- The class contains:
  - `fit()` → trains a Logistic Regression model (`solver="liblinear"`).  
  - `predict()` → generates predictions on unseen text.  
  - `evaluate()` → computes **accuracy**, **precision**, **recall**, and **F1-score** using weighted averages.  

### Step 4 — Baseline Testing
- Created `test/lab5_test.py` using a small toy dataset to verify model behavior.  
- Created `test/lab5_hf_sentiment.py` to train and evaluate on the real Hugging Face dataset.  

### Step 5 — Model Improvement (Task 4)
- Implemented an **improvement experiment** using one of the following:
  -  **Naive Bayes (MultinomialNB)** — better suited for sparse text data.  
  - or  
  -  **Advanced text preprocessing** (lemmatization and stopword removal).  
- Created a new test file: `test/lab5_improvement_test.py`.

---

## Code Execution Guide

### Environment Setup
```bash
pip install scikit-learn datasets pyspark nltk
