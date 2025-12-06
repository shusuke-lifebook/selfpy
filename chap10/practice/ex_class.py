class Hamuster:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def get_name(self) -> str:
        return self.__name

    def show(self, fmt):
        print(fmt.format(self.__name))


if __name__ == "__main__":
    h = Hamuster("のどか")
    h.show("私の名前は{0}です！")
