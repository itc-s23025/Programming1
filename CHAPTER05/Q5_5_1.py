a = {x for x in "abcabcabc" if x not in "ab"}
print(a)
# 集合の内包表記内の文字列'abcabcabc'がそれぞれ１文字ずつに分解されます。
# そのうち１文字ずつ分解されたｃが集合に追加されます。
# コードの正しい出力結果として{'C'}が出力されます。
