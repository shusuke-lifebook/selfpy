def log_func(func):
    def inner(*args, **keywds):
        print("----------")
        print(f"Name: {func.__name__}")
        print(f"Args: {args}")
        print(f"keywds: {keywds}")
        print("----------")
        return func(*args, **keywds)

    return inner


@log_func
def hoge(x, y, m="bar", n="piyo"):
    print(f"hoge: {x}-{y}/{m}-{n}")


hoge(10, 37, m="ほげ", n="ぴよ")
