import re

from bias_indicators import BiasIndicatorDetector


class SentenceAnalyzer:

    def __init__(self):
        self.detector = BiasIndicatorDetector()

    def split_sentences(self, text):
        """
        Split policy text into individual sentences.
        """

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

    def analyze_sentences(self, text):

        sentences = self.split_sentences(text)

        results = []

        for number, sentence in enumerate(
            sentences,
            start=1
        ):

            analysis = self.detector.analyze(
                sentence
            )

            # Only keep sentences containing
            # at least one indicator.
            if analysis["indicator_score"] > 0:

                results.append({

                    "sentence_number": number,

                    "sentence": sentence,

                    "loaded_words":
                        analysis["loaded_words"],

                    "strong_modal_words":
                        analysis["strong_modal_words"],

                    "uncertainty_words":
                        analysis["uncertainty_words"],

                    "indicator_score":
                        analysis["indicator_score"]
                })

        return results


if __name__ == "__main__":

    analyzer = SentenceAnalyzer()

    sample_text = """
    The government must protect vulnerable citizens.
    All applicants should receive equal opportunities.
    Dangerous activities may create serious risks.
    The policy provides financial assistance to students.
    """

    results = analyzer.analyze_sentences(
        sample_text
    )

    print("\nSENTENCE-LEVEL ANALYSIS")
    print("=" * 60)

    for result in results:

        print(
            f"\nSentence {result['sentence_number']}:"
        )

        print(result["sentence"])

        print(
            "Loaded words:",
            result["loaded_words"]
        )

        print(
            "Strong modal words:",
            result["strong_modal_words"]
        )

        print(
            "Uncertainty words:",
            result["uncertainty_words"]
        )

        print(
            "Indicator score:",
            result["indicator_score"]
        )
