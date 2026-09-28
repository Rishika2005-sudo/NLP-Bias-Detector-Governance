import re
from collections import Counter

from textblob import TextBlob


class PolicyLanguageAnalyzer:

    def __init__(self):

        # Words that may indicate strong or evaluative language.
        # These are indicators, NOT proof of bias.
        self.loaded_words = {
            "illegal",
            "dangerous",
            "threat",
            "unfair",
            "extreme",
            "radical",
            "problematic",
            "burden",
            "failure",
            "successful",
            "deserving",
            "undeserving",
            "vulnerable",
            "risky",
            "urgent"
        }

        # Words that can indicate uncertainty or modality.
        self.modal_words = {
            "may",
            "might",
            "could",
            "should",
            "must",
            "shall",
            "can",
            "would"
        }

    def clean_text(self, text):
        """
        Basic text cleaning.
        """

        text = text.lower()

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def get_words(self, text):
        """
        Convert text into words.
        """

        return re.findall(r"\b[a-zA-Z]+\b", text.lower())

    def detect_loaded_words(self, text):
        """
        Find words that belong to the loaded/evaluative
        vocabulary list.
        """

        words = self.get_words(text)

        found_words = [
            word for word in words
            if word in self.loaded_words
        ]

        return Counter(found_words)

    def detect_modal_words(self, text):
        """
        Find modal words such as may, should, must, etc.
        """

        words = self.get_words(text)

        found_words = [
            word for word in words
            if word in self.modal_words
        ]

        return Counter(found_words)

    def sentiment_analysis(self, text):
        """
        Calculate basic sentiment using TextBlob.
        """

        blob = TextBlob(text)

        return {
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity
        }

    def analyze(self, text):
        """
        Perform complete policy language analysis.
        """

        cleaned_text = self.clean_text(text)

        words = self.get_words(cleaned_text)

        loaded_words = self.detect_loaded_words(cleaned_text)

        modal_words = self.detect_modal_words(cleaned_text)

        sentiment = self.sentiment_analysis(cleaned_text)

        return {
            "word_count": len(words),
            "loaded_words": loaded_words,
            "modal_words": modal_words,
            "sentiment": sentiment
        }


if __name__ == "__main__":

    analyzer = PolicyLanguageAnalyzer()

    sample_text = """
    The government must protect vulnerable citizens.
    Dangerous activities may create serious risks.
    The policy should provide fair opportunities for all citizens.
    """

    results = analyzer.analyze(sample_text)

    print("\nPOLICY LANGUAGE ANALYSIS")
    print("-" * 50)

    print("Word count:")
    print(results["word_count"])

    print("\nPotential loaded/evaluative words:")
    print(results["loaded_words"])

    print("\nModal words:")
    print(results["modal_words"])

    print("\nSentiment:")
    print(results["sentiment"])
