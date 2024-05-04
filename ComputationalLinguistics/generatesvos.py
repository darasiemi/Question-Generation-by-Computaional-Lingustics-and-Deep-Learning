# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:25:59 2023

@author: Hp
"""



SUBJECT_DEPS = {"nsubj", "nsubjpass", "csubj", "agent", "expl", 'csubjpass'}
OBJECT_DEPS = {'dobj', 'iobj', 'pobj', 'attr', 'dative', 'oprd', 'date', 'advcl'}

# nlp = spacy.load("en_core_web_sm")
# for token in doc:
#     print(token.text, token.dep_, token.head.text, token.head.pos_,
#             [child for child in token.children] , [child for child in token.lefts], [child for child in token.rights])

#run this
# Get the token that is the root and break
# Loop through its children, 
    # find the first child of the root which is a subject
    # Store that as the subject
    # Find the next child that is an object type and store
    # And that is the subject verb object

# Take all the children of the subject, and that is the subject

def extract_svo(doc):
  for token in doc:
    if token.dep_ == "ROOT":
      root_token = token
      break
  # print(root_token)

  subj = None
  obj = None

  for child in root_token.children:
      # print(child)
      # print(child.dep_)
      if subj == None:
        if child.dep_ in SUBJECT_DEPS:
          subj = child
      else:
        if child.dep_ in OBJECT_DEPS:
          obj = child
          return subj, root_token, obj
