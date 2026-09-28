import csv
import os


class ResultsSaver:

    def save_summary(self, results, output_path):
        """
        Save policy analysis summary to a CSV file.
        """

        # Create output directory if it does not exist
        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        language = results["language_analysis"]

        row = {
            "pages": results["pages"],
            "word_count": language["word_count"],
            "loaded_words": str(
                language["loaded_words"]
            ),
            "modal_words": str(
                language["modal_words"]
            ),
            "sentiment_polarity": language[
                "sentiment"
            ]["polarity"],
            "sentiment_subjectivity": language[
                "sentiment"
            ]["subjectivity"]
        }

        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=row.keys()
            )

            writer.writeheader()
            writer.writerow(row)


if __name__ == "__main__":

    print("Results saver module ready.")
