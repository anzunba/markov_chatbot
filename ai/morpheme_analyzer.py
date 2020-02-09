from textblob import TextBlob
import MeCab
#from polyglot.text import Text

class MorphemeAnalyzer:
    # 形態素解析　TodayIsRainyDay => Today is Rainy Day
    def analyze(self, text, lang):
        if lang == 'ja':
            return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")
        elif lang == 'en':
            return text.replace("\n", " ").split(" ")

    # 名詞のみ抽出
    def extract_noun(self, text, lang):
        nouns = []
        if lang == 'ja':
            for chunk in MeCab.Tagger().parse(text).splitlines()[:-1]:
                (surface, feature) = chunk.split('\t')
                if feature.startswith('名詞'):
                    nouns.append(surface)
        elif lang == 'en':
            for i in TextBlob(text).tags:
                if i[1][:2] == "NN" or i[1] == "PRP":
                    nouns.append(i[0])
        return nouns 




        
        
