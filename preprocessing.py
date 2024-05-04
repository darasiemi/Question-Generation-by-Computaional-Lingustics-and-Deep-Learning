# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:01:11 2023

@author: Hp
"""

from coreferncing import resolved_paragraphs, nlp


sents = []
NER_tags = []
POS_tags = []
sents_tokens = []
# Split each paragraph into sentences using spacy
for paragraph in resolved_paragraphs:
    doc = nlp(paragraph)
    sentences = [sent.text for sent in doc.sents]
    sents.append(sentences)
    tokens = [sent for sent in doc.sents]
    sents_tokens.append(tokens)
    

    # Process each sentence
    for sentence in sentences:
        sent_doc = nlp(sentence)
        entities = [(ent.text, ent.label_) for ent in sent_doc.ents]
        NER_tags.append(entities)

    # Process each sentence
    for sentence in sentences:
        sent_doc = nlp(sentence)
        pos_tags = [(token.text, token.pos_) for token in sent_doc]
        POS_tags.append(pos_tags)
