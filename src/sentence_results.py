import csv
import os

from pdf_extractor import PDFTextExtractor
from text_cleaner import PolicyTextCleaner
from sentence_analysis import SentenceAnalyzer


class SentenceResultExporter:

    def __init__(self):
        self.pdf_extractor = PDFTextExtractor()
        self.cleaner = PolicyTextCleaner()
        self.analyzer = SentenceAnalyzer()

    def export(self, pdf_path, output_path):

        # Extract PDF
        pages = self.pdf_extractor.extract_text(
            pdf_path
        )

        # Combine pages
        full_text = " ".join(
            page["text"] for page in pages
        )

        # Clean text
        cleaned_text = self.cleaner.clean(
            full_text
        )

        # Analyze sentences
        results = self.analyzer.analyze_sentences(
            cleaned_text
        )

        # Create output directory
        directory = os.path.dirname(output_path)

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        # Save CSV
        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "sentence_number",
                "sentence",
                "loaded_words",
                "strong_modal_words",
                "uncertainty_words",
                "indicator_score"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for result in results:

                writer.writerow({
                    "sentence_number":
                        result["sentence_number"],

                    "sentence":
                        result["sentence"],

                    "loaded_words":
                        result["loaded_words"],

                    "strong_modal_words":
                        result["strong_modal_words"],

                    "uncertainty_words":
                        result["uncertainty_words"],

                    "indicator_score":
                        result["indicator_score"]
                })

        return len(results)


if __name__ == "__main__":

    pdf_path = (
        "data/raw/"
        "6219213_Draft_Final_Reservation_Guidelines---niu.pdf"
    )

    output_path = (
        "results/reports/"
        "sentence_level_analysis.csv"
    )

    exporter = SentenceResultExporter()

    count = exporter.export(
        pdf_path,
        output_path
    )

    print("\nSENTENCE-LEVEL RESULTS")
    print("=" * 60)

    print(
        "Flagged sentences:",
        count
    )

    print(
        "\nResults saved to:",
        output_path
    )
