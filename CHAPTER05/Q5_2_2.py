list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [x if x % 2 == 0 else None for x in list1]
print(list1)
# list1の各要素を２で割った余りが０のときと、それ以外のときを判定して、新しいリストを生成しようとしています。
# 新しいリストを生成し、それを変数に代入して元のlist1を更新します
# 正しい出力結果として[None,2,None,4,None,6,None,8,None]が出力されます。
