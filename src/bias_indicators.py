import re
from collections import Counter


class BiasIndicatorDetector:

    def __init__(self):

        # Potentially loaded or evaluative words.
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
            "deserving",
            "undeserving",
            "vulnerable",
            "risky",
            "urgent"
        }

        # Words that express obligation or strong modality.
        self.strong_modal_words = {
            "must",
            "shall",
            "should",
            "required",
            "need",
            "mandatory"
        }

        # Words that express uncertainty.
        self.uncertainty_words = {
            "may",
            "might",
            "could",
            "possibly",
            "perhaps",
            "likely",
            "unlikely"
        }

    def get_words(self, text):

        return re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )

    def detect_loaded_words(self, words):

        found = [
            word for word in words
            if word in self.loaded_words
        ]

        return Counter(found)

    def detect_strong_modal_words(self, words):

        found = [
            word for word in words
            if word in self.strong_modal_words
        ]

        return Counter(found)

    def detect_uncertainty_words(self, words):

        found = [
            word for word in words
            if word in self.uncertainty_words
        ]

        return Counter(found)

    def calculate_indicator_score(
        self,
        loaded_count,
        strong_modal_count,
        uncertainty_count
    ):

        score = (
            loaded_count * 2
            + strong_modal_count
            + uncertainty_count
        )

        return score

    def analyze(self, text):

        words = self.get_words(text)

        loaded = self.detect_loaded_words(words)

        strong_modal = self.detect_strong_modal_words(words)

        uncertainty = self.detect_uncertainty_words(words)

        score = self.calculate_indicator_score(
            sum(loaded.values()),
            sum(strong_modal.values()),
            sum(uncertainty.values())
        )

        return {
            "word_count": len(words),
            "loaded_words": dict(loaded),
            "strong_modal_words": dict(strong_modal),
            "uncertainty_words": dict(uncertainty),
            "indicator_score": score
        }


if __name__ == "__main__":

    detector = BiasIndicatorDetector()

    sample_text = """
    The government must protect vulnerable citizens.
    Dangerous activities may create serious risks.
    The policy should provide fair opportunities.
    """

    results = detector.analyze(sample_text)

    print("\nBIAS INDICATOR ANALYSIS")
    print("=" * 50)

    print("Word count:", results["word_count"])

    print("\nPotential loaded words:")
    print(results["loaded_words"])

    print("\nStrong modal words:")
    print(results["strong_modal_words"])

    print("\nUncertainty words:")
    print(results["uncertainty_words"])

    print("\nIndicator score:")
    print(results["indicator_score"])
