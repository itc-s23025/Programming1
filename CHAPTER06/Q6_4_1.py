f = open("some.txt")
c = 0
for i in f:
    print(i, end="")
    if c == 2:
        break
    c += 1
f.close()
