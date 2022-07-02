# 割り切れるiの和

def divisor():
    l = []
    for i in range(1,20000000):
        if 1234567890 % i == 0:
            l.append(i)
    print(sum(l))

divisor()