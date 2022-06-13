# B - Papers, Please
# https://atcoder.jp/contests/abc155/tasks/abc155_b

def immigration():
    n = int(input())
    a = list(map(int, input().split()))
    answer = "APPROVED"
    
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                answer = "DENIED"
    print(answer)

immigration()