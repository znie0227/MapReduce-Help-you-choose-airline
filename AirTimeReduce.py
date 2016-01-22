from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

f=open("test.txt","r")
for line in f:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = float(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
        
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
