import asyncio

async def fetch_data(url):
    print(f"请求{url}")
    await asyncio.sleep(1)
    return f"来自{url}的数据"
async def main():
    tasks = [fetch_data('url1'),fetch_data('url2')]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())

"""
    输出
    请求url1
    请求url2
    ['来自url1的数据', '来自url2的数据']
"""
