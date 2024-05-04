# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:27:16 2023

@author: Hp
"""

from coreferncing import resolved_paragraphs, nlp
from generatesvos import extract_svo
from questiontemplates import generate_when_question,generate_who_question,generate_what_question,generate_yes_or_no_question,generate_where_question, generate_subtree
from lemmainflection import verb_dict


all_svos = []
svos_texts = []
questions = []
for paragraph in resolved_paragraphs:
  doc = nlp(paragraph)
  for sentence in doc.sents:
  # doc = nlp(text)
    if extract_svo(sentence):
      sub, verb, obj = extract_svo(sentence)
      subject = generate_subtree(sub)
      objct = generate_subtree(obj)
      svos = (sub, verb, obj)
      svos_text = (subject,verb, objct)
      objct = generate_subtree(obj)
      svos_texts.append(svos_text)
      all_svos.append(svos)

      if verb.text in verb_dict.keys():
        if generate_when_question(svos,svos_text):
          question = generate_when_question(svos,svos_text)
          questions.append(question)
        if generate_where_question(svos,svos_text):
          question = generate_when_question(svos,svos_text)
          questions.append(question)

        if generate_who_question(svos,svos_text):
          question = generate_when_question(svos,svos_text)
          questions.append(question)
        if generate_what_question(svos,svos_text):
          question = generate_when_question(svos,svos_text)
          questions.append(question)
        if generate_yes_or_no_question(svos,svos_text):
          question = generate_when_question(svos,svos_text)
          questions.append(question)
