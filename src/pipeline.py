from pdf_extractor import PDFTextExtractor
from text_cleaner import PolicyTextCleaner
from preprocessing import TextPreprocessor
from policy_language import PolicyLanguageAnalyzer
from bias_indicators import BiasIndicatorDetector
from save_results import ResultsSaver


class PolicyBiasPipeline:

    def __init__(self):

        self.pdf_extractor = PDFTextExtractor()
        self.cleaner = PolicyTextCleaner()
        self.preprocessor = TextPreprocessor()
        self.language_analyzer = PolicyLanguageAnalyzer()
        self.bias_detector = BiasIndicatorDetector()
        self.results_saver = ResultsSaver()

    def analyze_pdf(self, pdf_path, output_path):

        # -----------------------------------
        # 1. Extract PDF text
        # -----------------------------------

        pages = self.pdf_extractor.extract_text(
            pdf_path
        )

        full_text = " ".join(
            page["text"] for page in pages
        )

        # -----------------------------------
        # 2. Clean text
        # -----------------------------------

        cleaned_text = self.cleaner.clean(
            full_text
        )

        # -----------------------------------
        # 3. NLP preprocessing
        # -----------------------------------

        processed_tokens = self.preprocessor.preprocess(
            cleaned_text
        )

        # -----------------------------------
        # 4. Policy language analysis
        # -----------------------------------

        language_results = self.language_analyzer.analyze(
            cleaned_text
        )

        # -----------------------------------
        # 5. Bias indicator analysis
        # -----------------------------------

        bias_results = self.bias_detector.analyze(
            cleaned_text
        )

        # -----------------------------------
        # 6. Combine results
        # -----------------------------------

        results = {

            "pages": len(pages),

            "original_text": full_text,

            "cleaned_text": cleaned_text,

            "processed_tokens": processed_tokens,

            "language_analysis": language_results,

            "bias_indicators": bias_results
        }

        # -----------------------------------
        # 7. Save results
        # -----------------------------------

        self.results_saver.save_summary(
            results,
            output_path
        )

        return results


if __name__ == "__main__":

    pdf_path = (
        "data/raw/"
        "6219213_Draft_Final_Reservation_Guidelines---niu.pdf"
    )

    output_path = (
        "results/reports/"
        "policy_analysis.csv"
    )

    pipeline = PolicyBiasPipeline()

    results = pipeline.analyze_pdf(
        pdf_path,
        output_path
    )

    print("\n")
    print("=" * 60)
    print("NLP BIAS DETECTOR FOR GOVERNANCE")
    print("=" * 60)

    print("\nPages analyzed:")
    print(results["pages"])

    print("\nProcessed tokens:")
    print(len(results["processed_tokens"]))

    print("\nPotential loaded words:")
    print(
        results["bias_indicators"]["loaded_words"]
    )

    print("\nStrong modal words:")
    print(
        results["bias_indicators"]["strong_modal_words"]
    )

    print("\nUncertainty words:")
    print(
        results["bias_indicators"]["uncertainty_words"]
    )

    print("\nLinguistic indicator score:")
    print(
        results["bias_indicators"]["indicator_score"]
    )

    print("\nSentiment:")
    print(
        results["language_analysis"]["sentiment"]
    )

    print("\nResults saved to:")
    print(output_path)
