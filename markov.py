#class for markov chains
#Zion Choi [4/2/2022]

import random
import re
import string

class markov:
    def __init__(self, filename='test.txt'):
        self.filename = filename
        self.dict = {}

    def read_file(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f]
        return lines

    def format_file(self, lines):
        #remove any whitespace/empty lines
        lines = [line for line in lines if line!='']

        #split the lines into single words and punctuation
        words = [word for list in [re.findall(r"[\w']+|[.,!?;]", line) for line in lines] for word in list]
        return words

    def create_markov(self):
        #run read and format
        words = self.format_file(self.read_file(self.filename))

        #initialize key:value pairs for dictionary, using 2D array to track value and frequency
        for word in words:
            self.dict[word] = []

        #checks for the next words and appends a list with [value, frequency] to the value
        #theoretically, by using frequencies instead of repeating elements, the size of the array is smaller
        #as the size of the txt files scale
        for key in self.dict.keys():
            #removes error for last index, not elegant but works
            try:
                next_words = [words[i+1] for i, j in enumerate(words) if j == key]
                for word in next_words:
                    if [word, next_words.count(word)] not in self.dict[key]:
                        self.dict[key].append([word, next_words.count(word)])
            except:
                pass

    def next_word(self, key):
        frequencies = (self.dict[key][i][1] for i in range(len(self.dict[key])))
        return random.choices(self.dict[key], weights=frequencies)[0][0]

    def format_sentence(self, sentence):
        formatted = ''
        for i in range(len(sentence)):
            if i == 0:
                formatted += sentence[i][0].upper()+sentence[i][1:]
            elif str(sentence[i]) in string.punctuation:
                formatted+=sentence[i]
            else:
                formatted+=' '+sentence[i]
        return formatted

    def create_sentence(self, word, sentence=[]):
        punctuation = '.?!'
        sentence.append(word)
        if word in punctuation:
            return self.format_sentence(sentence)
        return self.create_sentence(self.next_word(word), sentence)

    def generate_markov(self, words=120):
        keys = list(self.dict.keys())
        sentence_beginnings = [j for j in keys if j in [k[0] for k in self.dict['.']]]
        total = ''
        while len(total) < words:
            r = random.randint(0, len(sentence_beginnings)-1)
            if sentence_beginnings[r] in string.punctuation:
                pass
            else:
                total+=self.create_sentence(sentence_beginnings[r], []) +'\n'
        return total