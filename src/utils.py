class Analyzer:
    @staticmethod
    def count_sentences(text):
        # Replace ? and ! with . for consistence EOS syntax
        text = text.replace("?", ".")
        text = text.replace("!", ".")
        sentences = text.split('.')
        full_sentences = [sntc for sntc in sentences if len(sntc) > 0]
        return len(full_sentences)

    @staticmethod
    def count_characters(text):
        return len(text)

    @staticmethod
    def count_words(text):
        return len(text.split())
