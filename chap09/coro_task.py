import asyncio
import time


# ダミーの重い処理
async def heavy_process(name, sec):
    print(f"start {name}")
    await asyncio.sleep(sec)
    print(f"end {name}")
    return f"{name}/{sec}"


# 非同期処理のエントリーポイント
async def main():
    # print(await heavy_process("hoge", 2))
    # print(await heavy_process("bar", 5))
    # print(await heavy_process("piyo", 1))
    t1 = asyncio.create_task(heavy_process("hoge", 2))
    t2 = asyncio.create_task(heavy_process("bar", 5))
    t3 = asyncio.create_task(heavy_process("piyo", 1))
    print(await t1)
    print(await t2)
    print(await t3)


start = time.time()
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
