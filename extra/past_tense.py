# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:57:07 2017

@author: ayesha
"""

import nltk
#from example import ret_out
from nltk import regexp_tokenize
sent="I went"
suf=''
text=regexp_tokenize(sent,"[\w']+")
print text
print nltk.pos_tag(text)
suf=''
#text=ret_out()
#text=[('PRP', 'I'), ('VBG', 'going'), ('VBP', 'am')]
print text
c=0
k=0
#print len(text)
for i in range(0,(len(text))):
    x=nltk.pos_tag(text)[i][0]
    r={"VBP":1,
       "VBD":2,
       "VBG":2,
       "VBN":3,
    }
    if x in r:
        c=c+1
        k1=r[x]

y=nltk.pos_tag(text)[0][0]
s={
    "I":1,
    "We":2,
    "You":3,
    "She" or "He":4,
    "They":5,
  }
if y in s:
    k2=s[y]

if(k2==1):
    if(k1==1):
        suf="eechhi"
    elif(k1==2 and c==2):
        suf="uuthhili"
    elif(k1==2 and c==3):
        suf="aasutthili"
    elif(k1==3):
        suf="eethhili"
if(k2==2):
    if(k1==1):
        suf="uuchhu"
    elif(k1==2 and c==2):
        suf="uuthhile"
    elif(k1==2 and c==3):
        suf="aasutthile"
    elif(k1==3):
        suf="eethhile"
if(k2==3):
    if(k1==1):
        suf="uuchha"
    elif(k1==2 and c==2):
        suf="uuthhila"
    elif(k1==2 and c==3):
        suf="aasutthila"
    elif(k1==3):
        suf="eethhila"
if(k2==4):
    if(k1==2 and c==1):
        suf="eechhee"
    elif(k1==2 and c==2):
        suf="uuthhilaa"
    elif(k1==2 and c==3):
        suf="aasutthilaa"
    elif(k1==3):
        suf="eethhilaa" 
if(k2==5):
    if(k1==1):
        suf="uuchhanthi"
    elif(k1==2 and c==2):
        suf="uuthhile"
    elif(k1==2 and c==3):
        suf="aasutthile"
    elif(k1==3):
        suf="eethhile"
        
print("khaa"+suf)
