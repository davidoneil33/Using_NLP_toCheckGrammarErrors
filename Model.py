from textblob import TextBlob
import language_tool_python


class SpellCheckerModule:
    def __init__(self):
        self.spell_checker = TextBlob("")

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        tool = language_tool_python.LanguageTool("en-US")
        matches = tool.check(text)
        foundmistakes = []
        # Imprimindo as palavras erradas
        for match in matches:
            length = match.errorLength
            offset = match.offset
            error_word = text[offset : offset + length]
            foundmistakes.append(error_word)
        foundmistakes_count = len(foundmistakes)
        return foundmistakes, foundmistakes_count


if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I likes mashine learning. appplee is a fruist. bananana."
    print(obj.correct_spell(message))
    print(obj.correct_grammar(message))
