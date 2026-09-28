import re


class PolicyTextCleaner:

    def clean(self, text):
        """
        Clean extracted policy document text.
        """

        # Replace line breaks with spaces
        text = text.replace("\n", " ")

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove spaces before punctuation
        text = re.sub(r"\s+([.,;:!?])", r"\1", text)

        return text.strip()


if __name__ == "__main__":

    cleaner = PolicyTextCleaner()

    sample_text = """
    The government   must provide benefits
    to eligible citizens.
    
    The policy should ensure fair access .
    """

    cleaned_text = cleaner.clean(sample_text)

    print("\nCLEANED POLICY TEXT")
    print("-" * 50)

    print(cleaned_text)
