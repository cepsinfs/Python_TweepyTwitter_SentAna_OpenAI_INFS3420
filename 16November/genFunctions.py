import re
from textblob import TextBlob

def cleanText(text):
    text = re.sub('#', '', text)
    text = re.sub("RT[\s]+", '', text)
    text = re.sub("https?://\S+", '', text)
    text = re.sub("@[A-Za-z0-9]+:?", '', text)

    return text



def square(x):
    return x**2

def getAnalysis(polarity):
    if polarity < 0:
        return "Negative"

    elif polarity == 0:
        return "Neutral"

    elif polarity > 0:
        return "Positive"



def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity 