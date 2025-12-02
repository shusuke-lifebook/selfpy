# リストから順にファイルパスを取りだして、読み込みは委譲
def read_files(*files):
    for file in files:
        yield from read_lines(file)


# ファイル読み込みを行うサブジェネレーター
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


for line in read_files(
    "./chap09/sample1.dat", "./chap09/sample2.dat", "./chap09/sample3.dat"
):
    print(line)
