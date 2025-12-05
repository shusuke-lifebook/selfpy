import asyncio
import time

import aiohttp

# import requests


# 指定のURLにリクエストし、結果を取得
# async def get_content(url):
#     print(f"start {url}")
#     res = requests.request("get", url)
#     print(f"end {url}")
#     return res.text[:100]
async def get_content(url):
    print(f"start {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            text = await res.text()
    print(f"end {url}")
    return text[:100]


async def main():
    return await asyncio.gather(
        get_content("https://codezine.jp/"),
        get_content("https://wings.msn.to/"),
        get_content("https://www.web-deli.com/"),
    )


start = time.time()
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(
#     asyncio.gather(
#         get_content("https://codezine.jp/"),
#         get_content("https://wings.msn.to/"),
#         get_content("https://www.web-deli.com/"),
#     )
# )
result = asyncio.run(main())
end = time.time()
print(result)
print(f"Process Time: {end - start}")
