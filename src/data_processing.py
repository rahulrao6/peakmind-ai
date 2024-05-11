import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class DataProcessor:
    def __init__(self, data_path):
        """
        Initializes the DataProcessor with the path to the dataset.
        :param data_path: Path to the CSV file containing the data.
        """
        self.data = pd.read_csv(data_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def preprocess_data(self):
        """
        Cleans and preprocesses text data in the DataFrame and applies TF-IDF vectorization.
        """
        self.data['processed_summary'] = self.data['Summary'].apply(self._clean_and_lemmatize)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data['processed_summary'])

    def _clean_and_lemmatize(self, text):
        """
        Cleans and lemmatizes the text.
        :param text: str, text to preprocess
        :return: str, preprocessed text
        """
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text.lower())
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
        return ' '.join(lemmatized_tokens)

    def find_relevant_advice(self, user_input):
        """
        Finds the most relevant advice from the dataset based on the user input using cosine similarity.
        :param user_input: str, user input text
        :return: str, the most relevant advice text
        """
        processed_input = self._clean_and_lemmatize(user_input)
        user_tfidf_vector = self.vectorizer.transform([processed_input])
        cosine_similarities = cosine_similarity(user_tfidf_vector, self.tfidf_matrix).flatten()
        most_relevant_index = cosine_similarities.argmax()
        return self.data.iloc[most_relevant_index]['Summary']

# Example usage
if __name__ == "__main__":
    processor = DataProcessor('/Users/rahulrao/peakmind-ai/Compilation_T1_Master_Preprocessed.csv')
    processor.preprocess_data()
    user_input = "I am feeling overwhelmed with stress at work."
    advice = processor.find_relevant_advice(user_input)
    print("Relevant Advice:", advice)
