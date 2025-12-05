import asyncio
import time


async def heavy_process(name, sec):
    print(f"start {name}")
    await asyncio.sleep(sec)
    print(f"end {name}")
    return f"{name}/{sec}"


# gather をラップする async 関数を定義
async def main():
    return await asyncio.gather(
        heavy_process("hoge", 2),
        heavy_process("fuga", 5),
        heavy_process("piyo", 1),
        heavy_process("spam", 3),
    )


start = time.time()
result = asyncio.run(main())  # main() は Coroutine なので OK
end = time.time()

print(result)
print(f"Process Time: {end - start}")
