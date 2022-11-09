import re

def cleanText(text):
    text = re.sub('#', '', text)
    text = re.sub("RT[\s]+", '', text)
    text = re.sub("https?://\S+", '', text)
    text = re.sub("@[A-Za-z0-9]+:?", '', text)

    return text



def square(x):
    return x**2