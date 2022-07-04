import itertools

def takoyaki():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0

    # itertools.combinationsで、重複のない組み合わせを出力できる
    for (x, y) in itertools.combinations(a, 2):
        sum += x * y 
    print(sum)

takoyaki()