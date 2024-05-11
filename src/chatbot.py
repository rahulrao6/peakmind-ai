import openai
from sentiment_analysis import SentimentEmotionAnalyzer  # Make sure this is accessible

class TherapistChatbot:
    def __init__(self, openai_api_key):
        """
        Initializes the chatbot with the OpenAI API key and sets up the assistant.
        Uses GPT-4 for advanced conversational abilities and emotional intelligence.
        """
        self.api_key = openai_api_key
        self.assistant = None
        self.analyzer = SentimentEmotionAnalyzer()  # Initialize sentiment analyzer

    def setup_assistant(self):
        """
        Creates an Assistant instance with specific instructions.
        """
        try:
            self.assistant = openai.Assistant.create(
                model="gpt-4",
                instructions="You are a compassionate and understanding therapist. Listen carefully, provide support, and gently guide the conversation towards understanding the user's feelings and offering thoughtful advice.",
                api_key=self.api_key
            )
        except Exception as e:
            print(f"Failed to create assistant: {str(e)}")

    def generate_response(self, user_input):
        """
        Generates a response using the OpenAI Assistant based on user input.
        """
        if not self.assistant:
            self.setup_assistant()
            if not self.assistant:
                return "Assistant setup failed, cannot generate response."

        # Analyze sentiment before responding
        sentiment_results = self.analyzer.combined_analysis(user_input)
        print("Sentiment Analysis:", sentiment_results)  # Optionally log or display this information

        try:
            conversation = openai.Conversation.create(
                assistant_id=self.assistant.id,
                messages=[{"role": "user", "content": user_input}],
                api_key=self.api_key
            )

            latest_message = conversation.messages[-1] if conversation.messages else None
            response_text = latest_message['content'] if latest_message and latest_message['role'] == 'assistant' else "No response from assistant."
            return response_text
        except Exception as e:
            print(f"Error during response generation: {str(e)}")
            return "Sorry, I couldn't process that."

# Example usage
if __name__ == "__main__":
    api_key = "your-openai-api-key"
    chatbot = TherapistChatbot(api_key)
    user_input = "I've been feeling overwhelmed at work and it's starting to affect my home life."
    response = chatbot.generate_response(user_input)
    print("Therapist:", response)
