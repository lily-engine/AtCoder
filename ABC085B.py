def runrun():
    n = int(input())
    mochi = [int(input()) for i in range(n)]
    mochi.sort(reverse=True)
    # set()で重複する値を無視して、配列の要素を数える。
    count = len(set(mochi))
    print(count)

runrun()


# def runrun():
#     n = int(input())
#     mochi = [input() for i in range(n)]
#     # 文字列を数値の配列に変更
#     mochi = list(map(int, mochi))
#     # 大きい順に並べ替え
#     mochi.sort(reverse=True)
#     # set()で重複する値は無視する
#     count = len(set(mochi))
#     print(count)

# runrun()
