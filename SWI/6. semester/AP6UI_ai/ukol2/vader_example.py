# Pre-requisites:
# pip install nltk numpy

import numpy as np

# import nltk
# nltk.download('vader_lexicon')    # general sentiment analyzer
# nltk.download('punkt_tab')        # for tokenization

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

text = "This was bullshit. The movie started off with an intriguing premise. Seeing Demi Moore back on the big screen, portraying a character grappling with age-related insecurities, was both refreshing and powerful. Moore, as one of the most stunning and graceful mature actresses I've seen, brought a rawness to the role that really hit home. Her character's struggles with the pressure of maintaining physical beauty in a society obsessed with youth and appearance were deeply relatable, and it felt like the film was setting up to explore these important themes in a thoughtful and impactful way."
sentences = sent_tokenize(text)

sia = SentimentIntensityAnalyzer()

sentence_sentiments = [sia.polarity_scores(sentence) for sentence in sentences]

for i, sentiment in enumerate(sentence_sentiments):
    print(f"Sentence {i+1}: {sentences[i]}")
    print(f"Sentiment: {sentiment['compound']}")
    print("-" * 50)

print("Mean compound sentiment:", np.mean([sentiment['compound'] for sentiment in sentence_sentiments]))
print("Full sentiment result:", sia.polarity_scores(text))

