import tools
import settings

# By running the file:
# If the dependences are in the right place
# it will read the desired text and it will 
# output the number of paragraphs, sentences words,
# and the frequency of the words it has found.

# Also it will create a second output file
# Containing the same information but by removing stop words
# (aka words that does not give much meaning to the text)

# TODO: 
# Word Cloud
# Readme File
# Report
# move results and word cloud to output.py
# Add comments to the code


def main():
    fname = settings.filenames['fname']
    counter = tools.Counter(fname)
    counter.paragraph_tokenize()
    counter.sentences_tokenize()
    counter.word_tokenize()
    counter.results()




if __name__ == '__main__':
    main()