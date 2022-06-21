def polygon():
    n = int(input())
    a = list(map(int, input().split()))
    newlist = sorted(a, reverse=True)
    answer = "No"

    if newlist[0] < sum(newlist[1:n]):
        answer = "Yes"
    print(answer)

polygon()