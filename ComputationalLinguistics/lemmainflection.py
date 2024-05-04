# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:15:44 2023

@author: Hp
"""

from preprocessing import sents_tokens, NER_tags, POS_tags
from coreferncing import nlp 

from lemminflect import getLemma
from lemminflect import getInflection


#To get the root verbs of inflected verbs
verb_dict = {}
verb_dict2 = {}
for i in range(len(POS_tags)):
  for word, pos_tag in POS_tags[i]:
    # print(word)
    if pos_tag == "VERB":
      root_word = getLemma(word, upos='VERB')[0]
      verb_dict[word] = root_word
      root_word = nlp(word)[0].lemma_
      verb_dict2[word] = root_word
      
      
for i, pos2 in enumerate(zip(verb_dict.items(), verb_dict2.items())):
  
  word1, root_word1 = pos2[0]
  word2, root_word2 = pos2[1]
  if (root_word1==root_word2) == False:
    print(pos2)
