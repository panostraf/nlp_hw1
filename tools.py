
import settings
from nltk.tokenize import sent_tokenize

class Counter:
    def __init__(self, file_name):
        self.words = {}
        self.file_name = file_name
        self.str_file = open(self.file_name, 'r').read()

    def paragraph_tokenize(self):
        pars = [par for par in self.str_file.split('\n') if len(par) > 0]
        return len(pars)

    def sentences_tokenize(self):
        setences = sent_tokenize(self.str_file)
        return len(setences)

    def word_tokenize(self):
        words = [self.word_replacements(word) for word in self.str_file.split()]
        words = [word.split() for word in words]
        
        for word in words:
            
            if isinstance(word, list):
                print('True')
                for w in word:
                    print(w)
                    self.add_to_dict(w)
            else:
                self.add_to_dict(word)


    def word_replacements(self, item):
        item = self.punc_replacements(item)
        if item.isalnum()==False:
            for key in settings.rule_overide:
                item = item.replace(key, settings.rule_overide[key])
            for key in settings.replacement:
                item = item.replace(key, settings.replacement[key])
            return item

        else:
            return item
            
    def punc_replacements(self, word):

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
        if word in self.words.keys():
            self.words[word] += 1
        else:
            self.words[word] = 1

    def results(self):
        with open('results.txt','w') as f:
            
            text = f'''
Here are the results of the text:
Number of paragraphs:  {self.paragraph_tokenize()}\n
Number of sentences:  {self.sentences_tokenize()}\n
Number of words:  {sum(self.words.values())}\n
Number of unique words:  {len(self.words.keys())}\n
----------------------------------------
Here is the word frequency:
'''
            word_frequency = '\n'

            for key,value in self.sort_dict().items():
                word_frequency = word_frequency + f'{key} - {value}\n'

            f.writelines([text,word_frequency])

    def sort_dict(self):
        return dict(sorted(self.words.items(), key=lambda x: (-x[1], x[0])))

    def drop_stop_words(self):
        stop_words = settings.stop_words
        print(stop_words)
        print(len(self.words))
        for word in stop_words:
            try:
                self.words.pop(word)
            except KeyError:
                pass
        print(len(self.words))

