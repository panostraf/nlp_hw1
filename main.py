import tools
import settings


# TODO: 
# Word Cloud
# Readme File
# Report
# move results function to main.py
# Add comments to the code


def main():
    fname = settings.filenames['fname']
    counter = tools.Counter(fname)
    counter.paragraph_tokenize()
    counter.sentences_tokenize()
    counter.word_tokenize()
    
    counter.drop_stop_words()
    counter.results()



if __name__ == '__main__':
    main()