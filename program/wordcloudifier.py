#Take in user's long string of input, run the text against nltk, spit out a wordcloud
import re
import wordcloud as wc
import matplotlib.pyplot as plt
def myFunc():
	stopwords = open('stopwords.txt').read()
	stopwords_list = stopwords.split()

#Cleaning text for no punctuation.
	text = str(raw_input("Enter your text here."))
	lowercase = text.lower()
	nopunc = re.sub(r'[-./?!,":;()\']', ' ', lowercase)
	nopuncSplit = nopunc.split()

#Need to iterate through these words and match which AREN'T in stopwords list
	for i in nopuncSplit:
		if i in stopwords_list:
			nopuncSplit.remove(i)

	wordcloud = wc.WordCloud(width=1000, height=500).generate(' '.join(nopuncSplit))

	plt.figure(figsize=(15,8))
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

def addStopwords(words):
	toAdd = words.split()
	if toAdd not in stopwords_list:
		stopwords_list += toAdd

if __name__ == "__main__":
	myFunc()	
