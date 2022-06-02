def sunuke():
    # 例 3
    n = int(input())
    # 例 4 8 12
    arr = list(map(int,input().split()))
  
    count = 0
    boolean = True

    while boolean:
        # arrという配列の要素全てに実行するプログラムを書く
        # n回繰り返すfor文。（iに入るのは0,1,2)
        for i in range(n):
            if arr[i] % 2 == 0:
                arr[i] = arr[i]/2
            else:
                boolean = False

    # 上のmod計算で2で割り切れないとbooleanがFalseに変わる。
    # 逆に、全て2で割り切れればbooleanはTrueのまま。
        if boolean == True:
            count += 1

    # booleanがFalseに変わっていれば、while文から抜け出すことになる。
    print(count)

sunuke()