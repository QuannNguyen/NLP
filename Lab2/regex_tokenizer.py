from typing import List
from interfaces import Tokenizer
import re
class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        return tokens
    