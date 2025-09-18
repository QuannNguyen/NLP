from abc import ABC, abstractmethod
from typing import List


class Vectorizer(ABC):
    @abstractmethod
    def fit(self, corpus: List[str]):
        """
        Learn the vocabulary from a list of documents (corpus).
        """
        pass

    @abstractmethod
    def transform(self, documents: List[str]) -> List[List[int]]:
        """
        Transform a list of documents into a list of count vectors
        based on the learned vocabulary.
        """
        pass

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Convenience method: performs fit and then transform on the same data.
        """
        self.fit(corpus)
        return self.transform(corpus)

class Tokenizer(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        pass