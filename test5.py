# 1桁ことにばらして各桁の数字の積を求める

# 123 → 1 × 2 × 3 = 6
# 666 → 6 × 6 × 6 = 216
# 1024 → 1 × 0 × 2 × 4 = 0
# 任意の整数について、「操作」を繰り返し適用すると、最終的には一桁の数に到達します。

# 77 → 49 → 36 → 18 → 8
# 123456 → 720 → 0
# 一桁の数に到達するのに必要な「操作」の回数は、77では4回、123456では2回となります。
# それでは、1000000以下の整数のうち、一桁の数に到達するのに必要な「操作」の回数が3回となるものはいくつあるかを、求めてください。

import functools
import operator

def foo(num):
    count = 0
    while True: # ある条件を満たす間(Trueの間）、指定の処理を繰り返す
        lst = [int(i) for i in list(str(num))]
        if len(lst) == 1:
            return count
        # operator.mul(a,b)は、数値 a および b について a * b を返します（https://docs.python.org/ja/3/library/operator.html#operator.mul）
        num = functools.reduce(operator.mul, lst)
        count += 1

        # print(lst)をした場合、以下のように出力される。1桁になるまで割り算が繰り返されていることがわかる（〜1,000,000）。
        # [9, 9, 9, 9, 9, 9]
        # [5, 3, 1, 4, 4, 1]
        # [2, 4, 0]
        # [0]

if __name__ == '__main__':
    # [i for i in range(1000001) if foo(i) == 3] の数列には、3回の割り算で1桁になる数値が入る
    print(len([i for i in range(1000001) if foo(i) == 3]))

# functools
# https://docs.python.org/ja/3/library/functools.html#functools.reduce