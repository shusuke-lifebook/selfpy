class MyContext:
    # コンテキストの作成
    def __enter__(self):
        print("**Enter**")
        return self

    # コンテキストの開放
    def __exit__(self, type, value, tb):
        # 例外の有無を判定
        if type is None:
            print("**Exit**")
        else:
            print(f"**{value}**")
            return True

    def hoge(self):
        print("Hoge")


with MyContext() as c:
    print("With Start")
    c.hoge()
    # raise ValueError("値が不正です。")
