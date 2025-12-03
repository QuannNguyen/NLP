# Lab 6 Report: Named Entity Recognition (NER) with spaCy

## Objective  
Implement Named Entity Recognition (NER) to identify and classify entities (e.g., PERSON, ORG, LOCATION) in text using spaCy's pre-trained models, with optional custom training on a small annotated dataset.

## Methodology  

1. **Text Processing**  
   - Load spaCy's English model (`en_core_web_sm`).  
   - Process input text to extract entities via `doc.ents`.  
   - Visualize entities with `displacy` for rendering.  

2. **Entity Extraction**  
   - Labels: PERSON, ORG, GPE (geo-political), DATE, MONEY, etc.  
   - Custom training (if implemented): Use `spacy train` with example data in .spacy format.  

3. **Evaluation**  
   - Manual review on sample sentences.  
   - Metrics (for custom model): Precision, Recall, F1 per entity type using spaCy's scorer.  

Example code snippet (from `ner.py`):  
```python
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Sample usage
text = "Apple is looking at buying U.K. startup for $1 billion."
print(extract_entities(text))  # [('Apple', 'ORG'), ('U.K.', 'GPE'), ('$1 billion', 'MONEY')]
displacy.render(doc, style="ent", jupyter=False)
