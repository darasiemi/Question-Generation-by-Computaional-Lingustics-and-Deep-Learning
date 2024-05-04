# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:40:39 2023

@author: Hp
"""

from coreferencing import nlp

#Question filtering

# import spacy
from spacy.matcher import Matcher

# # Load the English language model
# nlp = spacy.load('en_core_web_sm')

# Define the rule-based patterns for questions
patterns = [
    [{'POS': 'NOUN'}, {'LOWER': 'is'}, {'POS': 'NOUN'}],
    [{'LOWER': 'what'}, {'POS': 'VERB'}, {'POS': 'DET'}, {'POS': 'NOUN'}],
    [{'LOWER': 'how'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}, {'LOWER': 'is'}, {'POS': 'NOUN'}]
]

# Create a Matcher object and add the patterns
matcher = Matcher(nlp.vocab)
matcher.add('Question', patterns, on_match=None)

# Define a function to filter the best question

def filter_questions(questions):
    
    filtered_questions = []
    # Create a list to store the scores for each question
    for question in questions:
        thresh = len(question) * 0.8
        doc = nlp(question)
        
        # Calculate the score for the question based on the number of matches
        score = len(matcher(doc))
        
        if score > thresh:
            filtered_questions.append(question)
            
    # Return the best question
    return filtered_questions