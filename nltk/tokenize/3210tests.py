import os
import sys
curdir = os.getcwd()    #assuming user is testing from nltk root folder
# curdir = curdir + "\\..\\.." #this line is if assuming user is testing from tokenizer folder
sys.path.insert(0, curdir) #add repo's nltk root to top of python sys.path

import nltk
from nltk import pos_tag, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

text = "Lorem ipsum dolor sit amet. consectetur adipiscing elit."
print("Input string 1:\n" + text + '\n');
text2 = "Lorem ipsum. . d.o.l.o.r sit amet@   @. consectetur!!!!!!!! adipiscing.... elit??."
print("Input string 2:\n" + text2 + '\n');

tagged_words = pos_tag(word_tokenize(text))
words = [word for word, tag in tagged_words]

tagged_words2 = pos_tag(word_tokenize(text2))
words2 = [word for word, tag in tagged_words2]
# print('x'+words[5]+'x')
print("Tokenized string 1:\n")
print(words)
print('\n')
print("New detokenized string 1:\n");
print(TreebankWordDetokenizer().detokenize(words) + '\n')
print("Period-isolated detokenized string 1:\n");
print(TreebankWordDetokenizer().detokenize(words, 0, 1) + '\n')



print("Tokenized string 2:\n")
print(words2)
print('\n')
print("New detokenized string 2:\n");
print(TreebankWordDetokenizer().detokenize(words2))
print("Period-isolated detokenized string 2:\n");
print(TreebankWordDetokenizer().detokenize(words2, 0, 1))