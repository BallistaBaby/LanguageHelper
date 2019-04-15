import string
#########################
#  LanguageHelper class
#########################

class LanguageHelper:

    def __init__ (self, languageFilename):
        self._words = set()
        with open(languageFilename) as data:
            line = data.readline()
            while line:
                line = line.rstrip()
                self._words.add(line)
                line = data.readline()

    def __contains__(self,query):
        if query in self._words:
            return True
        elif query.capitalize() in self._words:
            return True
        else:
            return False

    def getSuggestions(self,query):
        self._possible = []
        self._alphabet = list(string.ascii_lowercase)
        for i in range(len(query)):
            possible = query[:i] + query[(i+1):]
            self._possible.append(possible)
            for g in range(len(self._alphabet)):
                possible = self._alphabet[g]
                self._possible.append(possible)
        print(self._possible)

#########################
#  Unit Testing
#########################

if __name__ == '__main__':
    helper = LanguageHelper ('English.txt')

    if ('dogs' in helper):
        print ('Found "dogs"')

