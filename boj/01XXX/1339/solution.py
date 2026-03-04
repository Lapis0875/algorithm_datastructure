import io, os
from itertools import count

def count_words(text, counter):
    base = 1
    for c in reversed(text):
        counter[c] += base
        base *= 10

def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    N = int(input())
    scores = tuple(9 - i for i in range(10)) # 배수에 따른 숫자 할당표
    
    word_cnt = {}
    for _ in range(N):
        text = input().decode("utf-8").strip()
        count_words(text, word_cnt)
    order = sorted(word_cnt, key=lambda c: word_cnt[c], reverse=True)
    # 가장 배수가 높은 문자부터 9 ~ 0으로 숫자 할당 후 계산
    res = 0
    for i in range(len(order)):
        res += scores[i] * word_cnt[order[i]]
    print(res)
    
main()
