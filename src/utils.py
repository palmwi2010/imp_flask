class Analyzer:
    @staticmethod
    def count_sentences(text):
        # Replace ? and ! with . for consistence EOS syntax
        text = text.replace("?", ".")
        text = text.replace("!", ".")
        sentences = text.split('.')
        full_sentences = [sentence for sentence in sentences if len(sentence) > 0]
        return len(full_sentences)

    @staticmethod
    def count_characters(text):
        return len(text)

    @staticmethod
    def count_words(text):
        return len(text.split())

"""
For testing
analyzer = Analyzer()

test_str = "Happy days!!!!!! a. b. c."
print(f"Test text: {test_str}")
print(f"Sentence count: {analyzer.count_sentences(test_str)}")
print(f"Word count: {analyzer.count_words(test_str)}")
print(f"Character count: {analyzer.count_characters(test_str)}")
"""
