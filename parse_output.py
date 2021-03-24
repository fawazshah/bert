import json

with open('output.json') as f:
    data = json.load(f)

# data['linex_index'] is the number 0

# data['features'] is a list of feature objects
# Each feature object consists of:
# - token (str) - token at this index into the string
# - layers (list of objects)

# Each layer object contains:
# - index (int) - which layer this is in the BERT stack e.g. -1 is the final hidden layer
# - values (list of ints) - list of word embeddings at this layer


print(len(data['features'][0]['layers'][-1]['values']))
