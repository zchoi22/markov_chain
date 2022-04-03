#class for markov chains p2
#Zion Choi [4/2/2022]

import random
import re
import string

class markov2:
    def __init__(self, filename='test.txt', memory=2):
        self.filename = filename
        self.memory = memory
        self.sentence_beginnings = []

        self.words = self.format_file(self.read_file(self.filename))
        self.states = list(self.return_states(self.words))
        self.dict = {}

    def read_file(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f]
        return lines

    def format_file(self, lines):
        #remove any whitespace/empty lines
        lines = [line for line in lines if line!='']

        #split the lines into single words and punctuation
        words = [word.lower() for list in [re.findall(r"[\w']+|[.,!?;]", line) for line in lines] for word in list]
        return words

    def return_states(self, words):
        return set(words)

    def create_markov(self):
        for i in range(len(self.words)-self.memory-1):
            memory_set = [self.states.index(j) for j in self.words[i:i+self.memory+1]]
            key, value = tuple(memory_set[0:self.memory]), memory_set[-1]

            if self.states[key[0]] in '.!?':
                self.sentence_beginnings.append(tuple(memory_set[1:self.memory+1]))

            if key not in self.dict.keys():
                self.dict[key] = {}

            if value not in self.dict[key].keys():
                self.dict[key][value] = 0

            self.dict[key][value]+=1
        return self.dict

    def next_word(self, key):
        key = tuple([self.states.index(word.lower()) for word in key.split(' ')])
        frequencies = [self.dict[key][value] for value in self.dict[key].keys()]
        next_word = random.choices(list(self.dict[key].keys()), weights=frequencies)
        return self.states[next_word[0]]

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
        word = word.split(' ')
        sentence.append(word[0])
        if word[-1] in punctuation:
            sentence.append(' '.join(word[1:]))
            return self.format_sentence(sentence)
        return self.create_sentence(' '.join(word[1:]) + ' ' + self.next_word(' '.join(word)), sentence)

    def generate_markov(self, num_words=1000):
        keys = list(self.dict.keys())
        #sentence_beginnings = [j for j in keys if self.states.index('.') in self.dict[j].keys()]
        total = ''
        while len(total) < num_words:
            r = random.randint(0, len(self.sentence_beginnings)-1)
            if self.states[self.sentence_beginnings[r][-1]] in string.punctuation:
                pass
            else:
                words = ' '.join([self.states[word] for word in self.sentence_beginnings[r]])
                total+=self.create_sentence(words, []) +'\n'
        return total