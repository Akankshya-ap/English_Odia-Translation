import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import regexp_tokenize
import pandas as pd
path="/home/ayesha/Documents/machine translation/words_alpha.csv"
data=pd.read_csv(path)
data=data['word']
stemmer1=PorterStemmer()
lemma=WordNetLemmatizer()
for row1 in data:
    #list(row1)
    row1=row1.replace('\n','')
    x=stemmer1.stem(row1)
    y=lemma.lemmatize(row1)
    row1=regexp_tokenize(row1,"[\w']+")
    z=nltk.pos_tag(row1)
    #print row1
    #print z[0][0],z[0][1],x ,y#,z
