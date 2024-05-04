# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:12:16 2023

@author: Hp
"""

with open("/content/gdrive/MyDrive/NLPTemplateData/bulbasaur_pokemon.txt", "r") as file:
    text = file.read()
    # print(text)
paragraphs = text.split("\n\n")
