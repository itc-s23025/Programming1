import random
import string

name = "miyagi"

while True:
    # ランダムなアルファベットを生成
    random_letter = random.choice(string.ascii_uppercase)

    # 生成されたアルファベットを表示
    print(random_letter)

    # 名前の頭文字が表示されたらループを終了
    if random_letter == name[0].upper():
        break
