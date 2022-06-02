from tkinter import N

def sum_total():
    n,a,b = map(int,input().split())

    l = []
    for i in range(1,n+1):
        i_sum = sum(list(map(int,str(i))))
        if a <= i_sum <= b:
            l.append(i)
    l_sum = sum(l)
    print(l_sum)

sum_total()