import string
#########################
#  LanguageHelper class
#########################

class LanguageHelper:
    """A simple spell checking class"""

    def __init__ (self, languageFilename):
        """Initializes the set of all words in the english dictionary"""
        if not isinstance(languageFilename, str):
            raise TypeError('The filename must be a string')
        self._words = set()
        try:
            with open(languageFilename) as data:
                line = data.readline()
                while line:
                    line = line.rstrip()
                    self._words.add(line)
                    line = data.readline()
        except IOError:
            print('Please specify the correct name for the dictionary')

    def __contains__(self, query):
        if not isinstance(query, str):
            raise TypeError('The query must be a string')
        """Checks whether the query is a legitimate word"""
        if query in self._words:
            return True
        elif query.lower() in self._words:
            return True
        else:
            return False

    def getSuggestions(self,query):
        """Returns a sorted list of all legitimate language words that are precisely one edit away from the query."""
        if not isinstance(query, str):
            raise TypeError('The query must be a string')
        self._possible = []
        self._final = []
        self._alphabet = list(string.ascii_lowercase)
        self._alphabet.append('-')
        self._query = query.lower()
        for i in range((len(query))-1):
            possible = self._query[:i]+self._query[i+1]+self._query[i]+self._query[(i+2):]
            self._possible.append(possible)
        for i in range(len(query)):
            possible = self._query[:i] + self._query[(i+1):]
            self._possible.append(possible)
            for g in range(len(self._alphabet)):
                possible = self._query[:i]+self._alphabet[g]+self._query[(i+1):]
                possibleAlso = self._query[:i]+self._alphabet[g]+self._query[i:]
                self._possible.append(possible)
                self._possible.append(possibleAlso)
        suggestionLength = len(self._possible)
        for i in range(suggestionLength):
            self._possible.append(self._possible[i].capitalize())
        for i in self._possible:
            if i in self._words:
                if i not in self._final:
                    if i != query:
                        self._final.append(i)
        if query.istitle() == True:
            self._final = [i.capitalize() for i in self._final]
        self._final.sort()
        return self._final
        
#########################
#  Unit Testing
#########################

if __name__ == '__main__':
    helper = LanguageHelper ('English.txt')

    if ('dogs' in helper):
        print('Found "dogs"')

    if ('missouri' in helper):
        print('wrong')
    
    # Should print out Missouri
    print(helper.getSuggestions('Missouri'))
    print(helper.getSuggestions('missouri'))
   
    # Should print out a list containing words that are similar to 'test'
    print(helper.getSuggestions('tess'))

    # Should only print out capital words that are similar to 'test'
    print(helper.getSuggestions('Tess'))
    
    # Scans through all the words in a file. If are incorrect words, suggestions are given.
    def fileChecker(filename):
        translator = str.maketrans('', '', string.punctuation)
        allWords = []
        wrongWords = []
        listOfSuggestions = []
        try:
            with open(filename) as data:
                for line in data:
                    line = line.translate(translator) #Removes all punctuation
                    words = line.split()
                    for word in words:
                        allWords.append(word)
        except IOError:
            print('Please enter a valid filename')
        for i in allWords:
            if i not in helper:
                wrongWords.append(i)
        for x in wrongWords:
            listOfSuggestions.append(helper.getSuggestions(x))
        for i in range(len(wrongWords)):
            print('Word: ' + "'" + wrongWords[i] + "', " + 'List of Suggestions:', str(listOfSuggestions[i]))
        
    
    # Should give an error
    fileChecker('sampl.txt')

    # Checks for spelling errors in files
    fileChecker('sample.txt')
    fileChecker('sampleLetter.txt')

