import torch
import torch.nn as nn
import data

device = torch.device("cpu")

print("Load model......")

with open('model.pt', 'rb') as f:
    model = torch.load(f).to(device)
model.eval()

print("Load corpus......")

corpus = data.Corpus('./data/wikitext-2')
ntokens = len(corpus.dictionary)

print("Compute probabilities......")

def seq_prob(seq):
    prod_probs = 1
    softmax = nn.Softmax(dim=2)
    input =  # dictionary를 이용하여 모델에 입력되는 첫 번째 input 구성
    hidden =  # hidden값 초기화
    with torch.no_grad():
        for i in range(len(seq)-1):
            output, hidden =  # model로부터 실행 결과 얻기 
            word_weights =  # 각 단어별 확률
            prod_probs *= # 단어별 확률의 곱
    return prod_probs

print('P(the dog bark.) =', seq_prob(['the', 'dog', 'bark', '.']))
print('P(the cat bark.) =', seq_prob(['the', 'cat', 'bark', '.']))
print()
