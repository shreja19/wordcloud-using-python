#import all libraries
import regex as re
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class Book():
    def __init__(self, filename):
        self._text = ""
        self.book=filename
        self.words_dict = dict()    
        with open(self.book, encoding = 'utf-8') as f:
            self._text = self._text + " ".join(line.strip() for line in f)
         
        
    @property
    def length(self):
        return len(self._text)
    
    @property 
    def bookname(self):
        return self._bookname
    
    @bookname.setter
    def bookname(self,book_name):
        self._bookname = book_name
    
    def __repr__(self):
        return f'The file {self.book} is a {self._bookname} book which has {self.length} characters'
         
    def remove_punctuation_marks(self):
        self._text = re.sub(r'[^A-Za-z ]', '', self._text)
        self._text=self._text.lower()
        #remove single lettered words 
        self._text = re.sub(r"\b[a-z]\b", "", self._text)
    
        
    def apply_stemming(self):
        ps = PorterStemmer()
        words=word_tokenize(self._text)
        stem_word=[ps.stem(word) for word in words]
        self._text = " ".join(stem_word)
       
                
    def apply_lemmatization(self):
        
        blob=TextBlob(self._text)
        lemm_word=[word.lemmatize() for word in blob.words]
        self._text=" ".join(lemm_word)
   
        
    def remove_stopwords(self):
        sw = stopwords.words("english")
        wl = self._text.split()
        nsw = [word for word in wl if word not in sw]
        self._text = " ".join(nsw)
        
        
    def word_freq_counter(self):
        words = self._text.split()
        for w in words:
            if w in self.words_dict:
                self.words_dict[w] = self.words_dict[w] + 1
            else:
                self.words_dict[w] = 1
       
        self.words_dict = dict(sorted(self.words_dict.items(), key=lambda x:x[1], reverse=True))
       
      
    def generate_wordcloud(self):
       
        wc = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2')
        wc.generate_from_frequencies(self.words_dict)
        wc.to_file("pp-wordcloud.png")
        plt.figure(figsize=(10, 10))
        plt.axis("off")
        plt.imshow(wc)
        
    def bar_graph_top20_words(self, count=20):
                
        sorted_dict= dict(list(self.words_dict.items())[0:count])
        words=sorted_dict.keys()
        freq=sorted_dict.values()
        plt.figure(figsize=(10, 10))
        plt.bar(words,freq)
        plt.xticks(rotation=60)
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        
      
    def line_graph_sentiment_visualizer(self):
        
        uncleanText = open(self.book,encoding='utf-8').read()
        #removing all other special characters,numbers,white spaces except full stop 
        cleanText = re.sub('[^a-zA-Z\.]', ' ', uncleanText)
        blob=TextBlob(cleanText)
        sentences=blob.sentences
        number_of_sentences = len(sentences) 
        polarity=[s.sentiment.polarity for s in sentences]
        subjectivity=[s.sentiment.subjectivity for s in sentences]
        
        plt.figure(figsize=(10,10))
        line_chart1 = plt.plot(range(1,number_of_sentences+1), polarity,'b')
        line_chart2 = plt.plot(range(1,number_of_sentences+1), subjectivity,'g')
        plt.title('Sentiment Visualizer')
        plt.xlabel('Sentence Numbers')
        plt.ylabel('Sentence Sentiments')
        plt.legend(['polarity','subjectivity'], loc=4, shadow=True, fancybox=True)
        plt.show()
  
    
