class Localizer:
    def __init__(self, filename):
        self._translations = self.read_file(filename)

    def read_file(self, filename):
        word = ""
        lang = ""
        trans = {}
        with open(filename) as fh:
            for line in fh:
                line = line.strip()
                find = line.find("=")
                if find == -1:
                    word = line
                else:
                    lang = line[:find]
                    new = line[find+1:]
                    trans[(word, lang)] = new
        return trans

    def localize(self, word, lang):
        return self._translations.get((word, lang), word)

my_localizer = Localizer("localizations.txt")
my_localizer.localize("Cancel", "de")
print(my_localizer.localize("Cancel", "de"))

