# Lab 3.5 Report: Text Preprocessing and Sentiment Analysis Pipeline

## Objective  
Build a basic NLP pipeline for text preprocessing (tokenization, stemming, lemmatization, stopword removal) and simple sentiment analysis on movie reviews using a bag-of-words model with Naive Bayes classifier.

## Methodology  

1. **Text Preprocessing**  
   - **Tokenization**: Split text into words using NLTK's word_tokenize.  
   - **Normalization**: Convert to lowercase and remove punctuation.  
   - **Stopword Removal**: Filter out common English stopwords via NLTK.  
   - **Stemming/Lemmatization**: Apply Porter Stemmer or WordNet Lemmatizer to reduce words to base forms.  
   - **Vectorization**: Convert processed text to TF-IDF vectors using scikit-learn's TfidfVectorizer.  

2. **Sentiment Classification**  
   - Dataset: IMDb movie reviews (binary: positive/negative).  
   - Model: Multinomial Naive Bayes from scikit-learn.  
   - Train-test split: 80/20.  
   - Evaluation: Accuracy, Precision, Recall, F1-score.  

Example preprocessing snippet (from `preprocess.py`):  
```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in stopwords.words('english') and t not in string.punctuation]
    stemmer = PorterStemmer()
    return [stemmer.stem(t) for t in tokens]
