
filenames={'fname':'sample.txt',
			'output':'results.txt'}
            

replacement = {
				"n't":" not",
				"'ll":" will",
				"'ve": " have",
				"'re":" are",
				"'s":" s"
				}


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



puncuations = [ ':',
				'(',
				')',
				'*',
				'?',
				'.',
				',',
				'%',
				'^',
				'&',
				'@',
				'[',
				']',
				'<',
				'>',
				'-',
				'/',
				'\\',
				"'",
				'"',
				'!',
				"#",
				'$',
				'+',
				';',
				'<',
				'>',
				'=',
				'@',
				'[',
				']',
				'_',
				'|',
				'{',
				'}',
				'~',
				'΄',
				'`',
				'§'
				'±',
				'€',
				' '

				]

text = open('stop_words.txt','r')
stop_words = [word.strip() for word in text]
				