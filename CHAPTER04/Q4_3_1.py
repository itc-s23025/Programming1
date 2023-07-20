def concat_words(*args, separator="."):
    """任意の数の位置引数と区切り文字を受取、区切り文字でつなげる"""
    return separator.join(args)


# main
result = concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" ")
print(result)
