from pdf_extractor import PDFTextExtractor
from text_cleaner import PolicyTextCleaner
from preprocessing import TextPreprocessor
from policy_language import PolicyLanguageAnalyzer


class PolicyBiasPipeline:

    def __init__(self):
        self.pdf_extractor = PDFTextExtractor()
        self.cleaner = PolicyTextCleaner()
        self.preprocessor = TextPreprocessor()
        self.language_analyzer = PolicyLanguageAnalyzer()

    def analyze_pdf(self, pdf_path):

        # 1. Extract PDF text
        pages = self.pdf_extractor.extract_text(pdf_path)

        full_text = " ".join(
            page["text"] for page in pages
        )

        # 2. Clean text
        cleaned_text = self.cleaner.clean(full_text)

        # 3. NLP preprocessing
        processed_tokens = self.preprocessor.preprocess(
            cleaned_text
        )

        # 4. Policy language analysis
        language_results = self.language_analyzer.analyze(
            cleaned_text
        )

        return {
            "pages": len(pages),
            "original_text": full_text,
            "cleaned_text": cleaned_text,
            "processed_tokens": processed_tokens,
            "language_analysis": language_results
        }


if __name__ == "__main__":

    pdf_path = "data/raw/6219213_Draft_Final_Reservation_Guidelines---niu.pdf"

    pipeline = PolicyBiasPipeline()

    results = pipeline.analyze_pdf(pdf_path)

    print("\nPOLICY BIAS ANALYSIS PIPELINE")
    print("=" * 60)

    print("Number of pages:")
    print(results["pages"])

    print("\nNumber of processed tokens:")
    print(len(results["processed_tokens"]))

    print("\nPotential loaded/evaluative words:")
    print(results["language_analysis"]["loaded_words"])

    print("\nModal words:")
    print(results["language_analysis"]["modal_words"])

    print("\nSentiment:")
    print(results["language_analysis"]["sentiment"])
