n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = "Yes"

for i in range(m):
    if b[i] not in a:
        answer = "No"
        break
    # aの中にbの長さがあれば、以下の処理のみ実行。
    a.remove(b[i])

print(answer)

# PythonのCounterを使うと便利！