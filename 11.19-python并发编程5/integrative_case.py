"""
统计域名对应网页的大小并输出
"""

from multiprocessing import Pool
import requests
import os
import time

# 确保输出目录存在
os.makedirs("./output_files", exist_ok=True)

def get_page(url):
    print("<进程%s> get %s" % (os.getpid(), url))
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {
                "url": url,
                "text": response.text
            }
        else:
            return {
                "url": url,
                "text": "",
                "error": f"HTTP {response.status_code}"
            }
    except Exception as e:
        print(f"<进程{os.getpid()}> 请求 {url} 出错: {e}")
        return {
            "url": url,
            "text": "",
            "error": str(e)
        }

def parse_page(res):
    if res is None:
        print("警告：未收到结果")
        return
    if "error" in res:
        parse_res = f"url:<{res['url']}> error:[{res['error']}]\n"
    else:
        parse_res = f"url:<{res['url']}> size:[{len(res['text'])}]\n"
    with open("./output_files/db.txt", "a", encoding="utf-8") as f:
        f.write(parse_res)

if __name__ == "__main__":
    start = time.time()
    urls = [
        "https://www.baidu.com",
        "https://www.python.org"
    ]

    with Pool(4) as pool:
        async_results = [
            pool.apply_async(get_page, (i,), callback=parse_page)
            for i in urls
        ]
        # 等待所有任务完成
        results = [res.get() for res in async_results]

    print(f"耗时: {time.time() - start:.2f} 秒")