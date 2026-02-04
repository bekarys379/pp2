arr=[-1, "a", 8, 20, 43, "ow", "hi", 0, 2]

for x in arr:
    d=str(x)
    if d.isalpha():
        continue #function skips letters
    print(x)