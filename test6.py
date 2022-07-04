# たしかローマ数字で7桁になる数字の和、だったはず。解き終わらず。
# 参照：https://codom.hatenablog.com/entry/2017/01/26/000000
# 使わなかった案：https://masaki-note.com/2021/05/21/roman-to-integer/


def int2roman(n):
    1 <= n <= 1000
    s = []
    singles = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    doubles = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    triples = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    while n >= 1000:
        s.append('M')
        n -= 1000
    if 100 <= n <= 999:
        i = int(n / 100)
        s.append(triples[i-1])
        n -= i * 100
    if 10 <= n <= 99:
        i = int(n / 10)
        s.append(doubles[i-1])
        n -= i * 10
    if 1 <= n <= 9:
        s.append(singles[n-1])
    return "".join(s)

# def roman(s):
#     l = []
#     if len(s) == 7:
#         l.append(s)
#         print(sum(s))