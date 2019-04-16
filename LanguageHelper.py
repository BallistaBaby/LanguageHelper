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
        elif query.lower() in self._words:
            return True
        else:
            return False

    def getSuggestions(self,query):
        self._possible = []
        self._final = []
        self._alphabet = list(string.ascii_lowercase)
        self._alphabet.append('-')
        for i in range((len(query))-1):
            possible = query[:i]+query[i+1]+query[i]+query[(i+2):]
            self._possible.append(possible)
        for i in range(len(query)):
            possible = query[:i] + query[(i+1):]
            self._possible.append(possible)
            for g in range(len(self._alphabet)):
                possible = query[:i]+self._alphabet[g]+query[(i+1):]
                possibleAlso = query[:i]+self._alphabet[g]+query[i:]
                self._possible.append(possible)
                self._possible.append(possibleAlso)
        if query.islower() == True:
            suggestionLength = len(self._possible)
            for i in range(suggestionLength):
                self._possible.append(self._possible[i].capitalize())
        if query.istitle() == True:
            tempList = self._possible
            for i in self._possible:
                tempList = [i.lower() for i in self._possible]
            for i in tempList:
                self._possible = [i.capitalize() for i in tempList]
        for i in self._possible:
            if i in self._words:
                if i not in self._final:
                    self._final.append(i)
        self._final.sort()
        print(self._final)
        
#########################
#  Unit Testing
#########################

if __name__ == '__main__':
    helper = LanguageHelper ('English.txt')

    if ('dogs' in helper):
        print ('Found "dogs"')

