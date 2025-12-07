def init(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname


def show(self):
    print(f"私の名前は{self.lastname} {self.firstname}です！")


# Personクラスの定義
Person = type("Person", (object,), {"__init__": init, "show": show})

if __name__ == "__main__":
    p = Person("太郎", "山田")  # type: ignore
    p.show()  # type: ignore
    print(type(Person))
    print(isinstance(Person, type))
