import numpy as np
import logging
from textblob import TextBlob
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Set up basic logging
logging.basicConfig(level=logging.INFO)

class SentimentEmotionAnalyzer:
    def __init__(self):
        """
        Initializes the sentiment and emotion analysis pipelines. Pipelines are loaded during initialization,
        but you might want to consider loading them only when needed (lazy loading) if resource usage is a concern.
        """
        # Initialize sentiment analysis using Transformers
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        
        # Initialize emotion detection using Transformers
        self.emotion_pipeline = pipeline(
            "text-classification",
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )

    def analyze_basic_sentiment(self, text):
        """
        Analyzes polarity and subjectivity of the text using TextBlob.
        """
        blob = TextBlob(text)
        return {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}

    def analyze_detailed_sentiment(self, text):
        """
        Performs detailed sentiment analysis using a Transformers model.
        """
        try:
            result = self.sentiment_pipeline(text)[0]
            return result
        except Exception as e:
            logging.error(f"Error analyzing detailed sentiment: {e}")
            return {'error': str(e)}

    def detect_emotions(self, text):
        """
        Detects emotions from text using a specialized transformer model.
        """
        try:
            result = self.emotion_pipeline(text)[0]
            return result
        except Exception as e:
            logging.error(f"Error detecting emotions: {e}")
            return {'error': str(e)}

    def combined_analysis(self, text):
        """
        Combines basic sentiment, detailed sentiment, and emotion analysis for comprehensive insights.
        """
        basic_sentiment = self.analyze_basic_sentiment(text)
        detailed_sentiment = self.analyze_detailed_sentiment(text)
        emotion = self.detect_emotions(text)
        
        return {
            'basic_sentiment': basic_sentiment,
            'detailed_sentiment': detailed_sentiment,
            'emotion': emotion
        }

# Example usage
if __name__ == "__main__":
    analyzer = SentimentEmotionAnalyzer()
    text = "I'm extremely happy today, but a bit nervous about tomorrow's meeting."
    results = analyzer.combined_analysis(text)
    print(results)
