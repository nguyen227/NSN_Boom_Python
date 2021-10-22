class Test():
    def __init__(self) -> None:
        self.x = 0


t = Test()
d = {(1, 2): t}

d.setdefault()
if not d.get((1, 2)).x:
    print(2)
