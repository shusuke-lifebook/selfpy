class Figure:
    # width(幅)、height(高さ)を準備
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    # 面積を取得中身はダミー
    def get_area(self) -> int | float:
        return 0.0


class Triangle(Figure):
    # 三角形の面積を求めるためのget_areaメソッドを定義
    def get_area(self) -> int | float:
        return self.width * self.height / 2


class Rectangle(Figure):
    # 四角形の面積を求めるためのget_areaメソッドを定義
    def get_area(self) -> int | float:
        return self.width * self.height


if __name__ == "__main__":
    t = Triangle(10, 15)
    r = Rectangle(10, 15)
    print(t.get_area())
    print(r.get_area())
