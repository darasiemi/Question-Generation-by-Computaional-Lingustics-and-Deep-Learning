
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:31:21 2023

@author: Hp

"""

import spacy
from data_input import paragraphs

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('coreferee')

def coreference_resolution(doc):

  resolved_text = ""
  # print(doc)
  # doc._.coref_chains.print()
  for token in doc:
      repres = doc._.coref_chains.resolve(token)
      # print(repres)
      if repres:
          resolved_text += " " + " and ".join([t.text for t in repres])
      else:
          resolved_text += " " + token.text
      
  # print(resolved_text)

  return resolved_text

resolved_paragraphs = paragraphs.copy()

count = 0
for i in range(len(paragraphs)):
   document = nlp(paragraphs[i])
   new_paragraph = coreference_resolution(document)
  #  print(paragraphs[i])
  #  print("-------------")
   resolved_paragraphs[i] = new_paragraph
  #  print(new_paragraph)


