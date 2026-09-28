import ast
import os

import pandas as pd
import matplotlib.pyplot as plt


class BiasVisualizer:

    def __init__(self, csv_path, output_dir):
        self.csv_path = csv_path
        self.output_dir = output_dir

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

    def load_data(self):
        return pd.read_csv(self.csv_path)

    def count_words(self, series):

        counter = {}

        for value in series:

            if pd.isna(value):
                continue

            try:
                words = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                continue

            for word, count in words.items():

                counter[word] = (
                    counter.get(word, 0) + count
                )

        return pd.Series(counter).sort_values(
            ascending=False
        )

    def plot_loaded_words(self, data):

        counts = self.count_words(
            data["loaded_words"]
        )

        if counts.empty:
            print("No loaded words found.")
            return

        counts.head(10).plot(
            kind="bar",
            title="Most Frequent Potential Loaded Words"
        )

        plt.xlabel("Word")
        plt.ylabel("Frequency")
        plt.tight_layout()

        plt.savefig(
            f"{self.output_dir}/loaded_words.png"
        )

        plt.close()

    def plot_modal_words(self, data):

        counts = self.count_words(
            data["strong_modal_words"]
        )

        if counts.empty:
            print("No modal words found.")
            return

        counts.head(10).plot(
            kind="bar",
            title="Strong Modal Words"
        )

        plt.xlabel("Word")
        plt.ylabel("Frequency")
        plt.tight_layout()

        plt.savefig(
            f"{self.output_dir}/modal_words.png"
        )

        plt.close()

    def plot_uncertainty_words(self, data):

        counts = self.count_words(
            data["uncertainty_words"]
        )

        if counts.empty:
            print("No uncertainty words found.")
            return

        counts.head(10).plot(
            kind="bar",
            title="Uncertainty Words"
        )

        plt.xlabel("Word")
        plt.ylabel("Frequency")
        plt.tight_layout()

        plt.savefig(
            f"{self.output_dir}/uncertainty_words.png"
        )

        plt.close()

    def plot_indicator_scores(self, data):

        data["indicator_score"].plot(
            kind="hist",
            bins=10,
            title="Distribution of Linguistic Indicator Scores"
        )

        plt.xlabel("Indicator Score")
        plt.ylabel("Number of Sentences")
        plt.tight_layout()

        plt.savefig(
            f"{self.output_dir}/indicator_scores.png"
        )

        plt.close()

    def generate_all(self):

        data = self.load_data()

        self.plot_loaded_words(data)
        self.plot_modal_words(data)
        self.plot_uncertainty_words(data)
        self.plot_indicator_scores(data)

        print("\nVisualizations created successfully.")


if __name__ == "__main__":

    csv_path = (
        "results/reports/"
        "sentence_level_analysis.csv"
    )

    output_dir = "results/figures"

    visualizer = BiasVisualizer(
        csv_path,
        output_dir
    )

    visualizer.generate_all()
