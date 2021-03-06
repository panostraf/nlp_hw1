# --------------------------------------
# Author Trafalis Panagiotis
# Course : NLP
# HW#1
# ACG Ms DataScience
# --------------------------------------


import settings
import tools
from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# import settings

class Output(object):

    def __init__(self, n_pars,n_sent,word_dict,output_name):
        self.n_pars = n_pars
        self.n_sent = n_sent
        self.word_dict = word_dict
        self.output_name = output_name

        print('\n\nCheck directory results to see information about the text...')



# By running the file:
# If the dependences are in the right place
# it will read the desired text and it will 
# output the number of paragraphs, sentences words,
# and the frequency of the words it has found.

# Also it will create a second output file
# Containing the same information but by removing stop words
# (aka words that does not give much meaning to the text)

# TODO:


    def result_full_text(self):

        text = f"""
Number of paragraphs: {self.n_pars}
Number of sentences: {self.n_sent}
Number of words: {str(sum(self.word_dict.values()))}
Here is a word frequency {str(len(self.word_dict))}

        """
        
        text_2 = '\n'
        for key,value in self.word_dict.items():
            text_add = f'{str(key)}:{str(value)}\n'
            text_2 = text_2 + text_add
        
        with open(self.output_name,'w') as f:
            f.writelines([text,text_2])
        f.close()

        wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white'
                ).generate_from_frequencies(self.word_dict)

        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plt.savefig(self.output_name.replace('.txt','.png'))
        # plt.show()

