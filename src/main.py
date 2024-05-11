import os
from chatbot import TherapistChatbot
from sentiment_analysis import SentimentEmotionAnalyzer

def main():
    # Load configuration settings
    api_key = os.getenv('OPENAI_API_KEY', 'your-openai-api-key')

    # Initialize the chatbot with the OpenAI API key
    chatbot = TherapistChatbot(api_key)

    # Initialize the sentiment and emotion analyzer
    analyzer = SentimentEmotionAnalyzer()

    # Example user input
    user_input = "I've been feeling overwhelmed at work and it's starting to affect my home life."

    # Perform sentiment and emotion analysis
    sentiment_results = analyzer.combined_analysis(user_input)
    print("Sentiment and Emotion Analysis Results:", sentiment_results)

    # Generate and print response from the chatbot
    response = chatbot.generate_response(user_input)
    print("Therapist:", response)

if __name__ == "__main__":
    main()
