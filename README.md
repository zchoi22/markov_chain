# markov_chain

Markov class utilizes a dictionary where the keys represent different states, and values represent [value, frequency]. The model uses one word states, and uses the frequency values to generate the next word.

Markov2 class is more sophisticated, implementing memory to increase the complexity of states. For example, a memory of 2 stores a tuple of two words, rather than 1. This class also utilizes nested dictionaries, where keys represent states, and values are dictionaries with format {value, frequency}. The higher the memory, the more true to the initial text file the result will be.

To generate large amounts of predicted data, both classes utilize "starting words or phrases". Markov2, in addition, will continue to use the same text chain, until there are no tuples in the states, where it will pull from a starting phrase.
