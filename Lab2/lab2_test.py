import os
import tarfile
from regex_tokenizer import RegexTokenizer
from count_vectorizer import CountVectorizer
def main():
    
    tokenizer = RegexTokenizer()
    vectorizer = CountVectorizer(tokenizer)
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
    vectors = vectorizer.fit_transform(corpus)
    print("Vocabulary:", vectorizer.vocabulary_)
    print("Document-term matrix:")
    for vec in vectors:
        print(vec)
def load_raw_text_data(dataset_path):
    raw_texts = []
    with open(dataset_path, "r", encoding="utf-8") as f:
        doc = []
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            if not line:
                if doc:
                    raw_texts.append(" ".join(doc))
                    doc = []
                continue
            parts = line.split("\t")
            if len(parts) > 1:
                doc.append(parts[1])
        if doc:  
            raw_texts.append(" ".join(doc))
    return raw_texts


def main2():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    tar_path = os.path.join(BASE_DIR, "..", "datasets", "UD_English-EWT.tar.gz")
    extract_dir = os.path.join(BASE_DIR, "..", "UD_English-EWT")
    if not os.path.exists(extract_dir):
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=extract_dir)
    dataset_path = os.path.join(extract_dir, "UD_English-EWT", "en_ewt-ud-train.conllu")
    corpus = load_raw_text_data(dataset_path)

    tokenizer = RegexTokenizer()
    vectorizer = CountVectorizer(tokenizer)

    # Fit + transform
    vectors = vectorizer.fit_transform(corpus)

    print("Vocabulary size:", len(vectorizer.vocabulary_))
    print("First 20 vocab items:", dict(list(vectorizer.vocabulary_.items())[:20]))
    print("First 2 document vectors:", vectors[:2])

if __name__ == "__main__":
    main()
    main2()