
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
        g
        

#########################
#  Unit Testing
#########################

if __name__ == '__main__':
    helper = LanguageHelper ('English.txt')

    if ('dogs' in helper):
        print ('Found "dogs"')

