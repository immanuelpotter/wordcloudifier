#!/usr/bin/env python
#Take in user's long string of input, run the text against nltk, spit out a wordcloud
import re
import wordcloud as wc
import matplotlib.pyplot as plt

def read_stopwords(stopwords_file):
    try:
        stopwords = open(stopwords_file).read()
        stopwords_list = stopwords.split()
        return stopwords_list
    except IOError:
        return "That's not a text file!"

def user_text_and_clean():
    text = str(raw_input("Enter your text here.\n"))
    lowercase = text.lower()
    noPunc = re.sub(r'[-./?!,":;()\']', ' ', lowercase)
    noPuncSplit = noPunc.split()
    return noPuncSplit

def iterate():
    #Need to iterate through these words and match which AREN'T in stopwords list
    user_words=user_text_and_clean()
    stopwords_list=read_stopwords('stopwords.txt')
    i = 0
    n = len(list(user_words))
    while i < n:
        element = user_words[i]
	if element in stopwords_list:
            del user_words[i]
            n = n-1
        else:
            i = i+1
    return user_words


def display():
    user_words = iterate()
    wordcloud = wc.WordCloud(width=1000, height=500).generate(' '.join(list(user_words)))

    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    display()
