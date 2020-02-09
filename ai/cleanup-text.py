class ImportText:
    def __init__(self, fpath):
        self.fpath = fpath

    def read(self):
        return open(self.fpath, "r").read()

    def add(self, text):
        open(self.fpath, "a").write(text + "\n")
import_text = ImportText('library/import2.txt')
snake_text = ImportText('library/snake-text.txt')

a = import_text.read().split("\n")
for i in a:
    #data = i.split(":")
    #person = i.split(":")[0].strip()
    #quote = data[1]
    if i.split(":")[0].strip() == "Snake":
        text = i.split(":")[1]
        text = text.replace("?"," ?")
        #text = text.replace("?","")
        text = text.replace("."," .")
        #text = text.replace("!","")
        text = text.replace("!"," !")
        #text = text.strip() + " ."
        print(text)
        snake_text.add(text)









