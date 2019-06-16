def termFrequency(term,doc):
    term_in_document = doc.count(term.lower())
    len_of_document = float(len( doc))
    normalized_tf = term_in_document/ len_of_document
    return normalized_tf


def inverseTermFrequency(term, alldocs):
    import math
    num = 0
    docs = 0
    for doc in alldocs:
        if term.lower() in doc:
            num=num+1
    if num>0:
            total = len(alldocs)
            idf = math.log(float(total)/num)
            return idf
    else:
            return 0

 def main():
	f=open(r"C:\Users\Shalini\Documents\ll1.txt","r")#Enter name of document1 
	if f.mode == 'r':
    	contents0 = f.read()
	f=open(r"C:\Users\Shalini\Documents\ll2.txt","r")#Enter name of document2
	if f.mode == 'r':
    	contents00 = f.read()
	f=open(r"C:\Users\Shalini\Documents\ll3.txt","r")#Enter name of document3
	if f.mode == 'r':
    	contents3 = f.read()
	f=open(r"C:\Users\Shalini\Documents\ll4.txt","r")#Enter name of document4
	if f.mode == 'r':
    	contents4 = f.read()
	contents1 = []#creating the lists for tf
	contents1.append(contents0)
	contents1.append(contents00)
	contents1.append(contents3)
	contents1.append(contents4)
	contents2 = []#creating the lists for idf
	contents2.append(contents0)
	contents2.append(contents00)
	contents2.append(contents3)
	contents2.append(contents4)
	import nltk
	nltk.download()  
	from bs4 import BeautifulSoup 
	import re
	from nltk.corpus import stopwords
	i=0
	cleaned_contents1 = []
	while i<4:
    	example1 = BeautifulSoup(contents1[i])
    	letters_only = re.sub("[^a-zA-Z]", " ",example1.get_text() )
    	lower_case = letters_only.lower() 
    	words = lower_case.split() 
    	words = [w for w in words if not w in stopwords.words("english")]
    	cleaned_contents1.append(words)
    	i=i+1
	from bs4 import BeautifulSoup 
	import re
	from nltk.corpus import stopwords
	i=0
	modified_contents2 = []
	while i<4:
    	example1 = BeautifulSoup(contents2[i])
    	letters_only = re.sub("[^a-zA-Z]", " ",example1.get_text() )
    	lower_case = letters_only.lower() 
    	words = lower_case.split() 
    	words = [w for w in words]
    	modified_contents2.append(words)
    	i=i+1

    i=0
	while i<4:
    	for word in cleaned_contents1[i]:
        	tf = termFrequency(word,cleaned_contents1[i])
        	idf = inverseTermFrequency(word,modified_contents2[i])
        	print("Word:"+"  tf:"+"  idf:"+"   tf-idf")
        	print(word+"   "+str(tf)+"   "+str(idf)+"   "+str(tf*idf))
    	i=i+1