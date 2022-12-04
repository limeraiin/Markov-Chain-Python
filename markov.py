import random

targetLength = 16;  # This can be changed

# Read the input text from a file using the UTF-8 character encoding
with open("input.txt", encoding="utf-8") as f:
    input_text = f.read()

words = input_text.split()

markov_chain = {}
for i in range(len(words) - 2):
    bigram = (words[i], words[i+1])
    next_word = words[i+2]
    if bigram in markov_chain:
        markov_chain[bigram].append(next_word)
    else:
        markov_chain[bigram] = [next_word]

current_bigram = random.choice(list(markov_chain.keys()))
result = current_bigram[0] + " " + current_bigram[1]

while len(result.split()) < targetLength or result[-1] != ".":
    if current_bigram in markov_chain:
        next_word = random.choice(markov_chain[current_bigram])
        result += " " + next_word
        current_bigram = (current_bigram[1], next_word)
    else:
        break

print(result)
