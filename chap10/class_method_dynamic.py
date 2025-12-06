import types


# 動的に追加するメソッドを準備
def show_first(self):
    print(f"私の名前は{self.firstname}です！")


def show_last(self):
    print(f"私の名前は{self.lastname}です！")


# 初期状態では__init__/showメソッドだけです。
class Person:
    def __init__(self, fistname: str, lastname: str) -> None:
        self.firstname = fistname
        self.lastname = lastname

    def show(self) -> None:
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    p1 = Person("太郎", "山田")
    p2 = Person("次郎", "鈴木")
    # メソッドを動的に追加
    Person.show_first = show_first  # type: ignore
    p1.show_last = types.MethodType(show_last, p1)  # type: ignore
    p1.show_first()  # type: ignore
    p1.show_last()  # type: ignore
    p2.show_first()  # type: ignore
    p2.show_last()  # type: ignore
