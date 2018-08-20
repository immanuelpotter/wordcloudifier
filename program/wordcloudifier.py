#!/usr/bin/env python
#Take in user's long string of input, run the text against nltk, spit out a wordcloud
import re
import wordcloud as wcld
import matplotlib.pyplot as plt

class Wordcloudifier:
    def __init__(self,stopwords,user_words):
        try:
            stopwords_list = open(stopwords).read().split()
            self.stopwords_list = stopwords_list
            self.user_words = None
        except IOError:
            return "That's not a file!"

    def user_text_and_clean(self):
        text = str(raw_input("Enter your text here.\n"))
        lowercase = text.lower()
        noPunc = re.sub(r'[-./?!,":;()\']', ' ', lowercase)
        noPuncSplit = noPunc.split()
        self.user_words = noPuncSplit

    def get_stopwords_list(self):
        return self.stopwords_list

    def get_user_words(self):
        return self.user_words

    def iterate(self):
        #Need to iterate through these words and match which AREN'T in stopwords list
        i = 0
        n = len(list(self.user_words))
        while i < n:
            element = self.user_words[i]
            if element in self.stopwords_list:
                del self.user_words[i]
                n = n-1
            else:
                i = i+1
        return self.user_words


    def display(self):
        wordcloud = wcld.WordCloud(width=1000, height=500).generate(' '.join(list(self.user_words)))

        plt.figure(figsize=(15,8))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    wc = Wordcloudifier('stopwords.txt',None)
    wc.user_text_and_clean()
    wc.iterate()
    wc.display()
