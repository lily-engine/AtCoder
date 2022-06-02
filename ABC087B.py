# まずABCXをバラバラに受け取る

def combinations():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    count = 0
    # 2,2,2の場合
    # コードは上から実行されるので、i=0から始まる
    for i in range(a+1):
        # j=0から始まる
        for j in range(b+1):
            # k=0から始まる→次はi=0,j=0,k=1に→k=2でkのループが終わる→i=0,j=1,k=0（もう一度0に！）
            for k in range(c+1):
                sum = 500 * i + 100 * j + 50 * k
                if sum == x:
                    count += 1
    print(count)

combinations()