def cardGame():
    n = int(input())
    # input().split()で空白区切りの文字列を取得 → intに変換 → list関数で囲み、リストとしてaに設定
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    Alice_cards = a[0::2]
    Bob_cards = a[1::2]
    answer = sum(Alice_cards) - sum(Bob_cards)
    print(answer)

cardGame()