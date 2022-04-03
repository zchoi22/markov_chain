#serves as the extension and test file for the markov class
#Zion Choi [4/2/2022]

from markov import markov

def main():
    m = markov(filename='harry_potter.txt')

    #lines = m.read_file('test.txt')
    #words = m.format_file(lines)
    #print(lines, '\n'+str(words))

    m.create_markov()
    # a = []
    # for i in range(1000000):
    #     a.append(m.next_word('to'))
    # print(a.count('all'), a.count('fly'), a.count('get'))

    print(m.generate_markov(5000))

if __name__ == '__main__':
    main()