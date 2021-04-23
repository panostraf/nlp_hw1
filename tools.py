
import settings
from nltk.tokenize import sent_tokenize

class Counter:
    def __init__(self, file_name):
        self.words = {}
        self.paragraphs = 0
        self.sentences = 0
        self.unique_words = 0
        self.file_name = file_name
        self.str_file = open(self.file_name, 'r').read()


    def paragraph_counter(self):
        pars = [par for par in self.str_file.split('\n') if len(par) > 0]
        for pr in pars:
            self.paragraphs += 1
            self.sentences_counter(pr)


    def sentences_counter(self, par):
        setences = sent_tokenize(par)
        for sen in setences:
            self.word_counter(sen)
            self.sentences += 1


    def word_counter(self, sen):
        words = [self.word_replacements(word) for word in sen.split()]
        words = [word.split() for word in words]
        for word in words:
            if isinstance(word, list):
                for w in word:
                    self.punc_replacements(w)
            else:
                self.punc_replacements(word)


    def word_replacements(self, item):

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
                self.add_to_dict(word)
                break

        while word[-1:] in settings.puncuations:

            if len(word)>1:            
                self.add_to_dict(word[-1:])
                word = word[:-1]
            else:
                self.add_to_dict(word)
                break
                    
        self.add_to_dict(word)


    def add_to_dict(self, word):
        if word in self.words.keys():
            self.words[word] += 1
        else:
            self.words[word] = 1


    def results(self):
        with open('results.txt','w') as f:

            t0 = '''\nHere are the results of the text:\n'''
            t1=f'The number of paragraphs in text is:  {self.paragraphs}\n'
            t2=f'The number of sentences in text is:  {self.sentences}\n'
            t3=f'The number of words in text is:  {sum(self.words.values())}\n'
            t4=f'The number of unique words in text is:  {len(self.words.keys())}\n'
            t5 = '----------------------------------------'
            t6 = '\nHere is the word frequency:\n'
            f.writelines([t0,t1,t2,t3,t4,t5,t6])
            for key,value in self.sort_dict().items():
                    f.writelines(f'{key}:{value}\n')


    def sort_dict(self):
        dict_ = {}
        for w in sorted(self.words, key=self.words.get, reverse=True):
            my_item = (w, self.words[w])
            dict_[w] = self.words[w]
        return dict_
        # sorted_dict = sorted(self.words, key=self.words.get, reverse=True)
        # print(sorted_dict[10])


if __name__ == '__main__':
    fname = settings.filenames['fname']
    counter = Counter(fname)
    counter.paragraph_counter()
    counter.results()
