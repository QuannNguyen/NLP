import os
import tarfile
import pandas as pd
from simple_tokenizer import SimpleTokenizer
from regex_tokenizer import RegexTokenizer

text = "Hello, world! This is a test of the tokenizer modules."
text_2 = "NLP is fascinating... isn't it?"
text_3 = "Let's see how it handles 123 numbers and punctuation!"

def load_raw_text_data(dataset_path):
        raw_text = []
        with open(dataset_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("#") or line.strip() == "":
                    continue
                parts = line.split("\t")
                if len(parts) > 1:
                    raw_text.append(parts[1])
        return " ".join(raw_text)

def task1_2():

    # Use simple tokenizer
    print("Simple tokenizer output:")
    print(SimpleTokenizer().tokenize(text))
    print(SimpleTokenizer().tokenize(text_2))
    print(SimpleTokenizer().tokenize(text_3))

    # Use regex tokenizer
    print("\nRegex tokenizer output:")
    print(RegexTokenizer().tokenize(text))
    print(RegexTokenizer().tokenize(text_2))
    print(RegexTokenizer().tokenize(text_3))

def task3():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    tar_path = os.path.join(BASE_DIR,  "..","datasets", "UD_English-EWT.tar.gz")
    extract_dir = os.path.join(BASE_DIR, "UD_English-EWT")
    if not os.path.exists(extract_dir):
        with tarfile.open(tar_path, "r:gz") as tar:  # note the r:gz
            tar.extractall(path=extract_dir)

    # Folder to extract dataset
    dataset_path = os.path.join(extract_dir, "UD_English-EWT", "en_ewt-ud-train.conllu")
    raw_text = load_raw_text_data(dataset_path)
    sample_text = raw_text[:500]

    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    print(f"Original Sample: {sample_text[:100]}...")

    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()

    # Simple Tokenizer
    simple_tokens = simple_tokenizer.tokenize(sample_text)
    print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")

    # Regex Tokenizer
    regex_tokens = regex_tokenizer.tokenize(sample_text)
    print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")

    print(f"SimpleTokenizer token count: {len(simple_tokens)}")
    print(f"RegexTokenizer token count: {len(regex_tokens)}")
    print("\nSide-by-side comparison (first 20 tokens):")
    for i, (s, r) in enumerate(zip(simple_tokens[:20], regex_tokens[:20]), 1):
        print(f"{i:2d}. Simple: {s:15} | Regex: {r}")
        
if __name__ == "__main__":
    task1_2()
    task3()