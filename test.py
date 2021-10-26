a = {2: (3, 2), 3: (2, 2)}
for i in a:
    if a.get(i) == (3, 2):
        a.pop(i)

print(a)
