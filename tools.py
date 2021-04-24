
import settings
from nltk.tokenize import sent_tokenize
import nltk
import output

# nltk.download('punkt')
class Counter:
    def __init__(self, file_name):
        # Initialize global variables 
        self.words = {} # Dictionary for unique words
        self.words_rs = {} # Dictionary for unique words (no stop words)
        self.file_name = file_name # Input file from settings.py
        self.str_file = open(self.file_name, 'r').read()

    def paragraph_tokenize(self):
        # Split paragraphs on new lines and count only not null paragraphs 
        pars = [par for par in self.str_file.split('\n') if len(par) > 0]
        return len(pars)

    def sentences_tokenize(self):
        # Split sentences using nltk library
        setences = sent_tokenize(self.str_file)
        return len(setences)

    def word_tokenize(self):
        # Split words on space and apply word apply word_replacements function
        words = [self.word_replacements(word) for word in self.str_file.split()]
        # Because some items in list "words" are lists apply a split 
        # for each item 
        words = [word.split() for word in words] 
        
        for word in words:
            # In case there is a list inside the list "words" a third loop is required
            # Call add to dict method for each word to add them into the dictionary
            if isinstance(word, list):
                for w in word:

                    self.add_to_dict(w)
            else:
                self.add_to_dict(word)

        


    def word_replacements(self, item):
        # Returns a string or a list of strings
        # First calls the punc_replacement method
        item = self.punc_replacements(item)
        # Now all words have not punctuations at both sides
        if item.isalnum()==False:
            # If the word has any puncuation inside search in settings.py
            # replace all words that belong in rule_overide dictionary of settings.py
            # with the requested value
            for key in settings.rule_overide:
                item = item.replace(key, settings.rule_overide[key])
            # Finaly rest of constractions to the requested values
            for key in settings.replacement:
                item = item.replace(key, settings.replacement[key])
            return item

        else:
            return item

            
    def punc_replacements(self, word):
        # Takes as input a word and as long the word starts or ends with a
        # punctuation specified at settings.py file it will remove it
        # and it will add the punctuation to the unique word count dictionary
        # Finaly it returns a string with removed puncuations in order to be
        # proceced later.
        while word[0] in settings.puncuations:
            if len(word)>1:
                self.add_to_dict(word[0])
                word = word[1:]

            else:
                break

        while word[-1:] in settings.puncuations:
            if len(word)>1:            
                self.add_to_dict(word[-1:])
                word = word[:-1]
            else:
                break

        return word


    def add_to_dict(self, word):
        # Will check if word exists in dictionary and it will create a new key
        # if it does not exists, or it will increase the value by one if exists
        if word in self.words.keys():
            self.words[word] += 1
        else:
            self.words[word] = 1

    

    def sort_dict(self):
        # Sorts the dictionary by value and then my key
        return dict(sorted(self.words.items(), key=lambda x: (-x[1], x[0])))

    def sort_dict_stop(self):
        # Sorts the dictionary by value and then my key
        return dict(sorted(self.words_rs.items(), key=lambda x: (-x[1], x[0])))




    def drop_stop_words(self):
        # Read the stopwords file
        # Copy the dictionary words to dictionary words_rs
        # remove the stopword if exists in dictionary words_rs
        stop_words = settings.stop_words
        print('starting length:',len(self.words_rs))
        self.words_rs = self.words.copy()
        for word in stop_words:
            try:
                self.words_rs.pop(word)
                # print(word,'removed')
            except KeyError:
                # print('key error')
                pass

        print('final length: ',len(self.words_rs))




    def results(self):
        # Creates 2 result files, The first one contains the number of 
        # paragraphs, sentenses, words, and word frequency on the input document
        #
        # The second one provides the same information for but with stop words removed
        output1 = output.Output(
                    self.paragraph_tokenize(),
                    self.sentences_tokenize(),
                    self.sort_dict(),
                    settings.filenames['output'])
        output1.result_full_text()

        self.drop_stop_words()


        output2 = output.Output(
                    self.paragraph_tokenize(),
                    self.sentences_tokenize(),
                    self.sort_dict_stop(),
                    settings.filenames['output_2'])
        
        
        output2.result_full_text()
        # output2.result_rm_stopw()




