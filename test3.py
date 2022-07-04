# 3で割り切れるもの、もしくは数値に3が含まれるもの

sum = 0
for i in range(1,30001):
    if i % 3 == 0:
        sum += i
    elif '3' in str(i):
        sum += i
print(sum)