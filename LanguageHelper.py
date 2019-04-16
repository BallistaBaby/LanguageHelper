import string
#########################
#  LanguageHelper class
#########################

class LanguageHelper:
    """A simple spell checking class"""

    def __init__ (self, languageFilename):
        """Initializes the set of all words in the english dictionary"""
        self._words = set()
        with open(languageFilename) as data:
            line = data.readline()
            while line:
                line = line.rstrip()
                self._words.add(line)
                line = data.readline()

    def __contains__(self,query):
        """Checks whether the query is a legitimate word"""
        if query in self._words:
            return True
        elif query.lower() in self._words:
            return True
        else:
            return False

    def getSuggestions(self,query):
        """Returns a sorted list of all legitimate language words that are precisely one edit away from the query."""
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
        return self._final
        
#########################
#  Unit Testing
#########################

if __name__ == '__main__':
    helper = LanguageHelper ('English.txt')

    #if ('dogs' in helper):
    #    print('Found "dogs"')

    #if ('missouri' in helper):
    #    print('wrong')
    
    # Should print out Missouri
    #print(helper.getSuggestions('Missouri'))
    #print(helper.getSuggestions('missouri'))
   
    # Should print out a list containing words that are similar to 'test'
    #print(helper.getSuggestions('tess'))

    # Should only print out capital words that are similar to 'test'
    #print(helper.getSuggestions('Tess'))
    
    # Scans through all the words in a file. If are incorrect words, suggestions are given.
    def fileChecker(filename):
        translator = str.maketrans('', '', string.punctuation)
        allWords = []
        wrongWords = []
        listOfSuggestions = []
        with open(filename) as data:
            for line in data:
                line = line.translate(translator) #Removes all punctuation
                words = line.split()
                for word in words:
                    allWords.append(word)
        for i in allWords:
            if i not in helper:
                wrongWords.append(i)
        for x in wrongWords:
            listOfSuggestions.append(helper.getSuggestions(x))
        for i in range(len(wrongWords)):
            print('Words: ' + "'" + wrongWords[i] + "' " + 'List of Suggestions:', str(listOfSuggestions[i]))
        
                    
    fileChecker('sample.txt')

