import nltk
from nltk import CFG


grammar = CFG.fromstring("""
  S -> 'the' N | 'a' N
  N -> 'cat' | 'dog'
""")

parser = nltk.ChartParser(grammar)

for tree in parser.parse("the cat".split()):
    print(tree)
