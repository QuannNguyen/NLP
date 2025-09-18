import string
from typing import List
from interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        result = []
        temp = ''
        for char in text:
            if char in string.punctuation:
                if temp:
                    result.append(temp)
                    temp = ''
                result.append(char)
            else:
                temp += char
        if temp:
            result.append(temp)
        return result
        



