n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = "Yes"

for i in range(m):
    if b[i] not in a:
        answer = "No"
        break
    a.remove(b[i])

print(answer)

# PythonのCounterを使うと便利！