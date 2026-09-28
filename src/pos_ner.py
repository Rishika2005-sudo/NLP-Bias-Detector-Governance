import spacy


class PolicyTextAnalyzer:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, text):
        """
        Perform POS tagging and Named Entity Recognition.
        """

        doc = self.nlp(text)

        # POS tagging
        pos_tags = []

        for token in doc:
            pos_tags.append({
                "word": token.text,
                "pos": token.pos_,
                "description": token.tag_
            })

        # Named Entity Recognition
        entities = []

        for entity in doc.ents:
            entities.append({
                "text": entity.text,
                "label": entity.label_
            })

        return pos_tags, entities


if __name__ == "__main__":

    analyzer = PolicyTextAnalyzer()

    sample_text = """
    The Government of India introduced a new education policy
    in New Delhi in 2025. The policy aims to provide better
    opportunities for students across India.
    """

    pos_tags, entities = analyzer.analyze(sample_text)

    print("\nPOS TAGGING")
    print("-" * 50)

    for item in pos_tags:
        print(
            f"{item['word']:20} "
            f"{item['pos']:10} "
            f"{item['description']}"
        )

    print("\nNAMED ENTITIES")
    print("-" * 50)

    for entity in entities:
        print(
            f"{entity['text']:30} "
            f"{entity['label']}"
        )
