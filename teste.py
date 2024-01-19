from spellchecker import SpellChecker
import language_tool_python


class SpellCheckerModule:
    def __init__(self):
        self.spell_checker = SpellChecker()
        self.grammar_tool = language_tool_python.LanguageTool("en-US")

    def correct_spell(self, text):
        corrected_text = text
        for word in set(text.split()):
            # Corrige cada palavra e substitui no texto
            corrected_word = self.spell_checker.correction(word)
            corrected_text = corrected_text.replace(word, corrected_word)
        return corrected_text

    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)
        for match in sorted(matches, key=lambda m: m.offset, reverse=True):
            from_idx = match.offset
            to_idx = match.offset + match.errorLength
            suggested_correction = match.replacements[0] if match.replacements else ""
            text = text[:from_idx] + suggested_correction + text[to_idx:]
        return text


if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "One day i was playing with my fiends, they told my about his storyy. I raelly impressed"
    corrected_message = obj.correct_spell(message)
    corrected_message = obj.correct_grammar(corrected_message)
    print(corrected_message)
