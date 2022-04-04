#serves as the extension and test file for the markov class
#Zion Choi [4/2/2022]

from markov import markov
from markov2 import markov2

def main():
    #m = markov(filename='harry_potter.txt')
    m2 = markov2(filename='harry_potter.txt', memory=2)

    #lines = m.read_file('test.txt')
    #words = m.format_file(lines)
    #print(lines, '\n'+str(words))

    #m.create_markov()
    m2.create_markov()
    #print(m2.create_sentence('dying .', []))
    #print(m2.create_sentence('harry potter'))
    n = m2.generate_markov(num_words=10000)
    save_file = open('m2.txt', 'w')
    save_file.write(n)
    save_file.close()
    # a = []
    # for i in range(1000000):
    #     a.append(m.next_word('to'))
    # print(a.count('all'), a.count('fly'), a.count('get'))

    #print(m.generate_markov(5000))

if __name__ == '__main__':
    main()