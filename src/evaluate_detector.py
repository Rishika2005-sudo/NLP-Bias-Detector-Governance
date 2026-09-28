import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


INPUT_FILE = (
    "data/annotation/"
    "balanced_annotation_sample.csv"
)


def evaluate():

    data = pd.read_csv(INPUT_FILE)

    print("\nBIAS DETECTOR EVALUATION")
    print("=" * 60)

    # Show annotation status
    print("\nAnnotation status:")

    print(
        data["human_label"]
        .fillna("BLANK")
        .value_counts()
    )

    # Keep only labels that can be evaluated
    valid_labels = [
        "POTENTIAL_CONCERN",
        "NEUTRAL"
    ]

    evaluated_data = data[
        data["human_label"].isin(valid_labels)
    ].copy()

    # Check whether there is enough data
    if evaluated_data.empty:

        print(
            "\nNo completed annotations found."
        )

        print(
            "\nPlease fill the 'human_label' column in:"
        )

        print(
            INPUT_FILE
        )

        print(
            "\nAllowed labels:"
        )

        print("POTENTIAL_CONCERN")
        print("NEUTRAL")
        print("REVIEW")

        return

    # Automatic prediction
    evaluated_data["automatic_prediction"] = (
        evaluated_data["automatic_flag"]
        == "FLAGGED"
    ).astype(int)

    # Human ground truth
    evaluated_data["human_ground_truth"] = (
        evaluated_data["human_label"]
        == "POTENTIAL_CONCERN"
    ).astype(int)

    y_true = evaluated_data[
        "human_ground_truth"
    ]

    y_pred = evaluated_data[
        "automatic_prediction"
    ]

    # Metrics
    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    matrix = confusion_matrix(
        y_true,
        y_pred
    )

    print(
        "\nSentences evaluated:",
        len(evaluated_data)
    )

    print(
        "\nAccuracy:",
        round(accuracy, 3)
    )

    print(
        "Precision:",
        round(precision, 3)
    )

    print(
        "Recall:",
        round(recall, 3)
    )

    print(
        "F1-score:",
        round(f1, 3)
    )

    print("\nConfusion Matrix:")

    print(matrix)

    print(
        "\nClassification Report:"
    )

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=[
                "NEUTRAL",
                "POTENTIAL_CONCERN"
            ],
            zero_division=0
        )
    )


if __name__ == "__main__":

    evaluate()
