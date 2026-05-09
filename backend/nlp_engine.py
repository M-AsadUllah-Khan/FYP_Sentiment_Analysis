from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        category = "Positive"
    elif compound <= -0.05:
        category = "Negative"
    else:
        category = "Neutral"
        
    return category, compound, scores