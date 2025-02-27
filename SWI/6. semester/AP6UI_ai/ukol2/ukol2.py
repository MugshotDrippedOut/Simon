import requests
from bs4 import BeautifulSoup
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import numpy as np



class SentimentChecker:
    values = {'vpo':0.85,
              'pos':0.5,
              'neu':0,
              'neg':-0.4}
    
    def __init__(self, URL:str):
        self.URL = URL
        self.reviews = []
        self.title = ""
        self.wordFrequency = {}
        self.wordLenght = {}
        
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        self.title = (soup.find('a', attrs={'class':'sidebar-title'}).text).replace("\n", "").strip()
        self.reviewsTable = soup.find('div', attrs = {'id':'reviews'}) 
        
        
        for row in self.reviewsTable.find_all('div',
                         attrs = {'class':'review-row'}):   # Get every review row
            review = {}
            reviewText = (row.find('p').text).replace("\n", "")# Get reveiw text
            regex = re.compile('[^a-zA-Z ’]')               # Regex
            removeCharacters = regex.sub(' ', reviewText)   # Remove unwanted characters
            wordList = removeCharacters.split()             # Split review into words
            longestWord = (max(wordList ,key=len))          # Select longest word in the review
            
            # Check word frequency and lenght
            for word in wordList:
                    
                if word not in self.wordFrequency:
                    self.wordFrequency[word] = 1
                else:
                    self.wordFrequency[word] += 1
                
                if word not in self.wordLenght:
                    self.wordLenght[word] = len(word)
            
            
            # Add data to the reviews array
            review['author'] = regex.sub('',row.div.div.a.text).strip()
            review['review'] = reviewText
            review['sentiment'] = self.__getSentiment(reviewText)
            review['longestWord'] = longestWord
            
            self.reviews.append(review)
        
        # Sort word frequency
        self.wordFrequency = self.__sortDict(self.wordFrequency)
        self.wordLenght = self.__sortDict(self.wordLenght)
    
    # Get sentiment from text
    def __getSentiment(self, text):
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        return sentiment
    
    # Replace numver with word
    def __sentimentTranscript(self, sentiment):
        if (sentiment>self.values['vpo']):
            return "Very Positive"
        elif (sentiment>self.values['pos']):
            return "Positive"
        elif (sentiment>=self.values['neu']):
            return "Neutral"
        elif (sentiment>self.values['neg']):
            return "Negative"
        else:
            return "Very Negative"
    
    def __sortDict(self,dic:dict, reversed = True):
        return dict(sorted(dic.items(), key=lambda item: item[1], reverse=reversed))

    def __getCompound(self, review):
        return review['sentiment']['compound']
    
    def getTitle(self):
        return self.title    
    
    def meanSentiment(self):
        mean = np.mean([self.__getCompound(review) for review in self.reviews])
        return mean
    
    
    def distribution(self):
        positive = 0
        neutral = 0
        negative = 0
        for review in self.reviews:
            if self.__getCompound(review) > self.values['pos']:
                positive +=1
            elif self.__getCompound(review) >= self.values['neu']:
                neutral +=1
            else:
                negative +=1
        return positive,neutral,negative

    
    
    ## Print output values
    # howMuch variable declares how much data to be printed
    # 0 - only Title, URL, Number of reviews, mean
    # 1 - adding reviews 
    # 2 - adding top 10 longest and most frequent word
    def printReviews(self, howMuch:int = 2):
        nPositive, nNeutral, nNegative = self.distribution()
        print(f"Title: {self.getTitle()}")
        print(f"URL: {self.URL}")
        print(f"Number of reviews: {len(self.reviews)}")
        print(f"Positive:{str(nPositive).center(5)} Neutral:{str(nNeutral).center(5)} Negative:{str(nNegative).center(5)}")
        
        if (howMuch >0):
            for review in self.reviews:
                compound = self.__getCompound(review)
                print("-"*79)
                if (howMuch >0):
                    print(f"Autor: {review['author']}")
                print(f"Review: {review['review']}")
                print(f"Sentiment is {self.__sentimentTranscript(compound)} with score {compound}")
            print("-"*79)
        print(f"Mean compound sentiment was {self.__sentimentTranscript(self.meanSentiment())}: {self.meanSentiment()}")
        
        if (howMuch >1):
            print("="*79)
            print("Top 10 most frequent used words were:")
            wordsF = list(self.wordFrequency.items())[:10]
            for word in wordsF:
                print(f"{word[0]} : {word[1]}")
                
            print("="*79)
            print("Top 10 longest words that were used:")
            wordsL = list(self.wordLenght.items())[:10]
            for word in wordsL:
                print(f"{word[0]} : {word[1]} characters")
                
        print("- "*39+"-")


        
        

if __name__ == "__main__":
    URLs = ["https://www.rottentomatoes.com/m/captain_america_brave_new_world/reviews",
            "https://www.rottentomatoes.com/m/paddington_in_peru/reviews",
            "https://www.rottentomatoes.com/m/sonic_the_hedgehog_3/reviews",
            "https://www.rottentomatoes.com/m/forrest_gump/reviews",
            "https://www.rottentomatoes.com/m/catnado/reviews?type=user"]

    capAmerica = SentimentChecker(URLs[0])
    paddington = SentimentChecker(URLs[1])
    sonic = SentimentChecker(URLs[2])
    gump = SentimentChecker(URLs[3])

    capAmerica.printReviews(0)
    paddington.printReviews(0)
    sonic.printReviews(0)
    gump.printReviews(2)




