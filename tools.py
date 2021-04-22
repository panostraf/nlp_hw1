## In order to read only once the file
## First read it as one and split it in paragraphs
## For each paragrapgh split in sentenses
## For each sentence split in words

import settings
from nltk.tokenize import sent_tokenize

# a.Number of paragraphs
# b.Number of sentences
# c.Number of words (i.e., "tokens")
# d.Number of distinct words (i.e., "word types")
# e.List of word frequency counts.  Words are ordered by frequency (in the descending order), and words which have the same frequency count are ordered by lexicographical order (in the ascending order).
# f.Remove the stopwords (i.e., words that are frequent but do not contribute much to the meaning of a sentence.)  A list of stopwords is provided for English.
# g.How would what you did be different if you did it for another language (e.g. Greek or French). List as many changes in your approach as you can. Do you think there can be a universal methodology for identifying and counting words / sentences / paragraphs, or is it language specific?


class Counter:
    def __init__(self, file_name):
        self.words = {}
        self.paragraphs = 0
        self.sentences = 0
        self.unique_words = 0
        self.file_name = file_name
        self.str_file = open(self.file_name, 'r').read()


    def paragraph_counter(self):
        pars = [par for par in self.str_file.split('\n') if len(par)>0]
        
        for pr in pars:
            self.paragraphs +=1
            self.sentences_counter(pr)


    def sentences_counter(self, par):
        setences = sent_tokenize(par)
        for sen in setences:
            self.word_counter(sen)
            self.sentences+=1


    def word_counter(self, sen):
        words = [self.word_replacements(word) for word in sen.split()]
        words = [word.split() for word in words]
        words = [self.punc_replacements(word) for word in words]
        for word in words:
            print(word)
            if len(word)>1:
                for w in word:
                    self.add_to_dict(w)

            else:
                self.add_to_dict(word[0])
                

    def add_to_dict(self,word):
        if word in self.words.keys():
            self.words[word]+=1
        else:
            self.words[word] = 1


    def word_replacements(self,item):

        if item.isalnum() == False:
            for key in settings.rule_overide:
                item = item.replace(key,settings.rule_overide[key])


            for key in settings.replacement:
                item = item.replace(key,settings.replacement[key])

            return item

        else:
            return item

    def punc_replacements(self,word):
        for item in settings.puncuations:
            for w in word:
                words = w.split(item)
        return words


    def results(self):
        print('\n')
        print('--------------------------------------------------')
        print('The number of paragraphs in text is:', self.paragraphs)
        print('The number of sentences in text is:', self.sentences)
        print('The number of words in text is:', sum(self.words.values()))
        print('The number of unique words in text is:', len(self.words))
        self.sort_dict()
        

    def sort_dict(self):
        empty_list=[]
        for w in sorted(self.words, key=self.words.get, reverse=True):
            my_item = (w,self.words[w])
            print(my_item)
            empty_list.append(my_item)
        print(empty_list[:10])



if __name__ == '__main__':
    

    fname = settings.filenames['fname']
    counter = Counter(fname)
    counter.paragraph_counter()
    counter.results()

    
