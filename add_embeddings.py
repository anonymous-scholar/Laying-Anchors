import math
import torch
import random
import pickle
import numpy as np
from tqdm import tqdm
from random import sample
from decimal import Decimal
from transformers import BertConfig, BertForMaskedLM, BertTokenizerFast

with open('./WikiText103/nums', 'rb') as fp:
    numerals = pickle.load(fp)

numerals = [int(x) for x in numerals if round(math.log(int(x), 10)) < 10]
numerals = sorted(list(set(numerals)))

_100 = sorted(numerals[:100])

train_100 = []
for i in tqdm(range(800)):
    sam = random.sample(_100, 2)
    sam.append(sum(sam))
    train_100.append(sam)
    
test_100 = []
for i in tqdm(range(200)):
    sam = random.sample(_100, 2)
    sam.append(sum(sam))
    test_100.append(sam)

print("test_100 : {} and train_100 : {} samples.".format(len(test_100), len(train_100)))

# 100-1000
_1000 = numerals[100:1000]
train_1000 = []
for i in tqdm(range(800)):
    sam = random.sample(_1000, 2)
    sam.append(sum(sam))
    train_1000.append(sam)
    
test_1000 = []
for i in tqdm(range(200)):
    sam = random.sample(_1000, 2)
    sam.append(sum(sam))
    test_1000.append(sam)

#1000 to 10k
_10000 = []
for i in list(range(1000,10001)):
    if i in numerals:
        _10000.append(i)


train_10k = []
for i in tqdm(range(800)):
    sam = random.sample(_10000, 2)
    sam.append(sum(sam))
    train_10k.append(sam)
    
test_10k = []
for i in tqdm(range(200)):
    sam = random.sample(_10000, 2)
    sam.append(sum(sam))
    test_10k.append(sam)

train_B10k, test_B10k = [], []
_B10k = numerals[4852:]

for i in tqdm(range(800)):
    sam = random.sample(_B10k, 2)
    sam.append(sum(sam))
    train_B10k.append(sam)
    
for i in tqdm(range(200)):
    sam = random.sample(_B10k, 2)
    sam.append(sum(sam))
    test_B10k.append(sam)

train, test = [], []
train.extend(train_100)
train.extend(train_1000)
train.extend(train_10k)
train.extend(train_B10k)

test.extend(test_100)
test.extend(test_1000)
test.extend(test_10k)
test.extend(test_B10k)


def get_embeddings_add(tokenizer_path, model_path, numbers_list, save_path)
    tokenizer = BertTokenizerFast.from_pretrained(tokenizer_path)
    model = BertForMaskedLM.from_pretrained(model_path, output_hidden_states=True)

    X = []
    y = []

	for i in tqdm(numbers_list):
	    X_sub = []
	    for j in i[:-1]:
	        input_ids = torch.tensor(tokenizer.encode(str(j))).unsqueeze(0)
	        outputs = model(input_ids)
	        last_four = torch.stack(outputs['hidden_states'][-4:]).sum(0)
	        emb = last_four[0][1:-1].mean(dim=0)
	        X_sub.append(emb.detach().numpy())
	    X.append(np.concatenate((X_sub[0], X_sub[1])))
	    y.append(i[-1])

    with open(save_path + /'X', 'wb') as fp:
        pickle.dump(X, fp)
    with open(save_path + /'y', 'wb') as fp:
        pickle.dump(y, fp)


def main():
    #Call the function for the respective model embeddings you'd like
    #The global variables defined cover numerals from 1 to 10^10 for addition task
    pass

if name == '__main__':
    main()