class Test():
    def __init__(self) -> None:
        self.x = 0


t = Test()
d = {(1, 2): t}

if not d.get((1, 2)).x:
    print(2)
