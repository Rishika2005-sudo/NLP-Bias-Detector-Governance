import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("stopwords")
nltk.download("wordnet")


class TextPreprocessor:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        """
        Basic text cleaning.
        """

        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove special characters and numbers
        text = re.sub(r"[^a-zA-Z\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def tokenize(self, text):
        """
        Split text into individual words.
        """

        return text.split()

    def remove_stopwords(self, tokens):
        """
        Remove common English stopwords.
        """

        return [
            word for word in tokens
            if word not in self.stop_words
        ]

    def lemmatize(self, tokens):
        """
        Convert words to their base form.
        """

        return [
            self.lemmatizer.lemmatize(word)
            for word in tokens
        ]

    def preprocess(self, text):
        """
        Complete preprocessing pipeline.
        """

        text = self.clean_text(text)

        tokens = self.tokenize(text)

        tokens = self.remove_stopwords(tokens)

        tokens = self.lemmatize(tokens)

        return tokens


if __name__ == "__main__":

    processor = TextPreprocessor()

    sample_text = """
    The government has introduced a new policy
    to provide benefits to citizens.
    """

    result = processor.preprocess(sample_text)

    print("Original text:")
    print(sample_text)

    print("\nProcessed tokens:")
    print(result)
