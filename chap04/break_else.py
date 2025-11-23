data = ["さくら", "うめ", "ききょう", "くちなし", "ぼたん"]

for name in data:
    # 要素が「ｘ」の場合にループを終了
    if name == "ｘ":
        break
    print(name)
else:
    print("正常終了しました。")
