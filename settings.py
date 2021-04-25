# --------------------------------------
# Author Trafalis Panagiotis
# Course : NLP
# HW#1
# ACG Ms DataScience
# --------------------------------------

# By changing the values of this dict 
# you can specify which file the algorithm will read (fname)
# The name of the output file (output)
# and the name of the stopwords file (stop_words)

# Please only change the values and not the keys of the dict
# And only the names after "/" as prion to slash it refers to folder name
# As it may break the code
filenames={'fname':'inputs/sample.txt',
			'output':'results/results.txt',
			'output_2':'results/results2.txt',
			'stop_words':'inputs/stop_words.txt'}


            

# Here you can set rules to replace contractions
# You can add new or remove existing ones
replacement = {
				"n't":" not",
				"'ll":" will",
				"'ve": " have",
				"'re":" are",
				"'s":" s"
				}

# Here you can set rules of that will be applied for given replacements
# This has higher priority than replacement dict, 
# Which means that if a key exists in the text it will transformed to the
# specified value
rule_overide = {
				"won't":"will not",
				"Won't":"Will not",
				"can't":"can not",
				"Can't":"Can not",
				"I'm":"I am",
				"i'm":"i am",
				"he's":"he is",
				"she's":"she is",
				"it's":"it is",
				"He's":"He is",
				"She's":"She is",
				"It's":"It is",
				"that's":"that is",
				"here's":"here is",
				"there's":"there is",
				"That's":"That is",
				"Here's":"Here is",
				"There's":"There is",
				}


# Here you can set all the puncuations that you want the 
# algorithm to remove from the sides (start and end) of each word
# They will also be counted as a word
puncuations = [ ':',
'(', ')', '*', '?',
'.', ',', '%', '^',
'&', '@', '[', ']',
'<', '>', '-', '/',
'\\', "'", '"', '!',
"#", '$', '+', ';',
'<', '>', '=', '@',
'[', ']', '_', '|',
'{', '}', '~', '΄',
'`', '§', '±', '€',
' ']

# Do not change this values, the name of the text file cointaining stop words,
# can be specified at the top of the file in filenames dict
text = open(filenames['stop_words'],'r')
stop_words = [word.strip() for word in text]
				