#serves as the extension and test file for the markov class
#Zion Choi [4/2/2022]

from markov import markov
from markov2 import markov2

def main():
    #m = markov(filename='harry_potter.txt')
    m2 = markov2(memory=3)

    #lines = m.read_file('test.txt')
    #words = m.format_file(lines)
    #print(lines, '\n'+str(words))

    #m.create_markov()
    print('done')
    m2.create_markov()
    #print(m2.create_sentence('harry potter'))
    print(m2.generate_markov(num_words=1000))
    # a = []
    # for i in range(1000000):
    #     a.append(m.next_word('to'))
    # print(a.count('all'), a.count('fly'), a.count('get'))

    #print(m.generate_markov(5000))

if __name__ == '__main__':
    main()