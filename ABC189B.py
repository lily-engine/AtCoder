def alcoholic():
    n,x = map(int,input().split())
    total = 0
    ans = -1
    for i in range(n):
        a, b = map(int, input().split())
        total += a * b
        if total > x * 100:
            ans = i+1
            break
    print(ans)

alcoholic()