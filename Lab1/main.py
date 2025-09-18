
import pandas as pd
from simple_tokenizer import SimpleTokenizer
from regex_tokenizer import RegexTokenizer
text = "Hello, world! This is a test of the tokenizer modules."
text_2 = "NLP is fascinating... isn't it?"
text_3 = "Let's see how it handles 123 numbers and punctuation!"

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

