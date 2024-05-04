# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:36:12 2023

@author: Hp
"""

from transformers import T5ForConditionalGeneration, T5TokenizerFast
from data_inputs import paragraphs

from training import tokenizer

hfmodel = T5ForConditionalGeneration.from_pretrained("/content/gdrive/MyDrive/QG_squad")


def hf_run_model(input_string, **generator_args):
  generator_args = {
  "max_length": 3081,
  "num_beams": 4,
  "length_penalty": 1.5,
  "no_repeat_ngram_size": 3,
  "early_stopping": True,
  }
  input_string = "generate questions: " + input_string + " </s>"
  input_ids = tokenizer.encode(input_string, return_tensors="pt")
  res = hfmodel.generate(input_ids, **generator_args)
  output = tokenizer.batch_decode(res, skip_special_tokens=True)
  output = [item.split("<sep>") for item in output]
  return output


questions = []
for paragraph in paragraphs:
  questions.append(hf_run_model(paragraph))

questions = []
for question_list in questions:
  for quest in question_list:
    if len(quest) > 1:
      for question in quest:
        questions.append(question)