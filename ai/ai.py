import re

from ai.import_text import ImportText
from ai.markov import Markov
from ai.morpheme_analyzer import MorphemeAnalyzer
from ai.fixed_phrase import FixedPhrase
from textblob import TextBlob

class Ai:
    lang = ''
    def input_answer(input_text):
        import_text = ImportText('library/snake-text.txt')
        fixed_phrase = FixedPhrase('library/pattern.csv')
        morpheme_analyzer = MorphemeAnalyzer()
        #lang = TextBlob(input_text).detect_language()
        ja_regex = u'[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]|[ぁ-んァ-ヶ]'
        #en_regex = '[a-zA-Z]'
        default_message = ""
        if (re.match(ja_regex, input_text)):
            lang = 'ja'
            default_message = "すみません。回答は限られています。他のことを聞いてみてください。"
        else:
            lang = 'en'
            default_message = "I'm sorry. My responses are limited. Ask me something else."
        markov = Markov(morpheme_analyzer.analyze(import_text.read(), lang))


        # ユーザー入力をインポートテキストに追記する
        if (re.match('@|＠', input_text)):
            add_text = re.sub('^@|^＠', '', input_text)
            import_text.add(add_text)
            markov.add(morpheme_analyzer.analyze(add_text, lang))
            output_text = "覚えたぞ！"
        else:
            # 定型文から回答を取得
            output_text = fixed_phrase.answer(input_text, lang)

        # 定型文の回答がなければユーザー入力の名詞を起点にマルコフ連鎖で回答
        if output_text == "":
            nouns = morpheme_analyzer.extract_noun(input_text, lang)
            output_text = markov.answer(nouns, lang).capitalize()

        if output_text == "" or output_text == " ":
            output_text = default_message
        return output_text
