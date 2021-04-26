 Author: Panagiotis Trafalis
 Student: ACG Ms Data Science
 Course: NLP
 Homework: HW1



 The algorithm takes as input a .txt file with the text and a .txt with stop words.
 
 What it does:
 It will read and process the text, and output 2 .txt files:
 The first one cointains the number of paragraphs, sentenses, words and the word frequency
 The second one will contain the same information but with stop words removed
 
 It will also create to word_could pictures in .png, one using all the words and one using the words with out stop-words.


 Structure:
 
 By default it contains a folder inputs and a folder results.
 Inside the folder inputs place the file with the text that will be analyzed and the file with the stop-words.
 The results folder is empty, and after the code execution the results will be saved inside.
 The rest of the files are in the main directory. There is no need to move them.


 Set UP:
 
 1) File set up
 There are 2 ways to set up the algorithm, either rename the input files as ( sample.txt for the text file and stop_words.txt for the stop-words file )
 or place these 2 files inside the folder inputs and open the settings.py file. Inside settings there is a dictionary called filenames. Rename the fname 
 (the key of the    dictionary) to the name of the file.
 
 2) Execute for first time
 In order to execute the code just run the main.py file.
 The first time that is running, in file tools.py near the top of the file under the imports section, there is a command nltk.download('punkts').
 This command has to be comment out after the first execution of the code since it is not necessary any mode.
 
 
 Notes:
 
 It is recommened to use a virtual enviroment.
 There is a file requirements.txt with all the dependencies.
 
 
