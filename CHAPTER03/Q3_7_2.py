with open("number.txt", "r") as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)
# 1から10の数字が書かれたファイルを１行ずつ読み込んで、その数値を合計した結果を表示しています。
