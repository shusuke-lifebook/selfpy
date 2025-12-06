class MyCalss:
    def __init__(self, kind: str, name: str) -> None:
        self.kind = kind
        self.name = name

    def show(self):
        return f"ペットの{self.kind}の名前は、{self.name}です。"


class MySubClass(MyCalss):
    def show(self):
        return f"[{super().show()}]"


if __name__ == "__main__":
    ms = MySubClass("ハムスター", "のどか")
    print(ms.show())
