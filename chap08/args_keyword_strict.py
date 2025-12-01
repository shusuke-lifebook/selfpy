# arg2,3はキーワード引数であること
def my_func(arg1, *, arg2, arg3):
    pass


# my_fun(1, 2, 3) # エラー
my_func(1, arg2=2, arg3=3)
