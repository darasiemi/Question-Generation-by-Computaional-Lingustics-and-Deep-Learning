# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:22:00 2023

@author: Hp
"""
from lemmainflection import verb_dict

def generate_when_question(svos, svo_text):
  sub, verb, obj = svos
  sub_text, verb_text, obj_text = svo_text
  tags = ["DATE", "TIME"]
  question = ""
  print("obj")
  print(obj.ent_type_)
  print("subj")
  print(sub.ent_type_)
  
  if obj.ent_type_ in tags:
     question = "When did " + sub_text + " " + verb_dict[verb.text] + " " + obj_text + " ?"
  

  return question 


def generate_where_question(svos,svo_text):
  sub, verb, obj = svos
  sub_text, verb_text, obj_text = svo_text

  tags = ["GPE", "FAC", "ORG"]
  question = ""

  print("obj")
  print(obj.ent_type_)
  print("subj")
  print(sub.ent_type_)
  
  
  if obj.ent_type_ in tags:
    question = "Where did " + sub_text + " " +verb_dict[verb.text] + "?"

  return question 

def generate_who_question(svos, svo_text):
  sub, verb, obj = svos
  sub_text, verb_text, obj_text = svo_text
  tags = ["ORG", "PERSON"]
  question = ""

  print("obj")
  print(obj.ent_type_)
  print("subj")
  print(sub.ent_type_)
  

  if sub.ent_type_ in tags:
    question = "Who did " + sub_text + " " + verb_dict[verb.text] + "?"

  return question 

def generate_what_question(svos, svo_text):
  sub, verb, obj = svos
  sub_text, verb_text, obj_text = svo_text
  tags = ["PRODUCT",     "EVENT",     "WORK_OF_ART",     "LAW",     "LANGUAGE", "MONEY",  "PERCENT",   "QUANTITY",     "ORDINAL",     "CARDINAL"]
  question = ""

  print("obj")
  print(obj.ent_type_)
  print("subj")
  print(sub.ent_type_)
  
  if obj.ent_type_ in tags:
    question = "What did " + sub_text + " " + verb_dict[verb.text] + "?"


  return question

def generate_yes_or_no_question(svos, svo_text):
  sub, verb, obj = svos
  sub_text, verb_text, obj_text = svo_text

  question = ""
  
  print("obj")
  print(obj.ent_type_)
  print("subj")
  print(sub.ent_type_)
  
  if obj and sub:
      question = "Did" + sub.text + " " + verb_dict[verb.text] + " " + obj.text + " " + "?"

  return question

def generate_subtree(token):
  subtree = ""
  for i in token.subtree:
    subtree += i.text_with_ws

  return subtree

