from concurrent.futures import ThreadPoolExecutor
from threading import Lock, current_thread

# 共享变量
counter = 0
lock = Lock()


def task():
    global counter
    with lock:
        old_value = counter
        counter += 1
        print(f"[{current_thread().name}] {old_value} → {counter}")


if __name__ == "__main__":
    print("开始执行 100 个并发任务（使用 10 个工作线程）...\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task) for _ in range(100)]

        for future in futures:
            future.result()

    print(f"\n 最终计数：{counter}")

"""
输出
    [ThreadPoolExecutor-0_0] 0 → 1
    [ThreadPoolExecutor-0_1] 1 → 2
    [ThreadPoolExecutor-0_0] 2 → 3
    [ThreadPoolExecutor-0_0] 3 → 4
    [ThreadPoolExecutor-0_1] 4 → 5
    [ThreadPoolExecutor-0_1] 5 → 6
    [ThreadPoolExecutor-0_4] 6 → 7
    [ThreadPoolExecutor-0_4] 7 → 8
    [ThreadPoolExecutor-0_3] 8 → 9
    [ThreadPoolExecutor-0_6] 9 → 10
    [ThreadPoolExecutor-0_6] 10 → 11
    [ThreadPoolExecutor-0_6] 11 → 12
    [ThreadPoolExecutor-0_6] 12 → 13
    [ThreadPoolExecutor-0_6] 13 → 14
    [ThreadPoolExecutor-0_6] 14 → 15
    [ThreadPoolExecutor-0_6] 15 → 16
    [ThreadPoolExecutor-0_6] 16 → 17
    [ThreadPoolExecutor-0_6] 17 → 18
    [ThreadPoolExecutor-0_6] 18 → 19
    [ThreadPoolExecutor-0_6] 19 → 20
    [ThreadPoolExecutor-0_6] 20 → 21
    [ThreadPoolExecutor-0_6] 21 → 22
    [ThreadPoolExecutor-0_6] 22 → 23
    [ThreadPoolExecutor-0_6] 23 → 24
    [ThreadPoolExecutor-0_6] 24 → 25
    [ThreadPoolExecutor-0_6] 25 → 26
    [ThreadPoolExecutor-0_6] 26 → 27
    [ThreadPoolExecutor-0_6] 27 → 28
    [ThreadPoolExecutor-0_6] 28 → 29
    [ThreadPoolExecutor-0_6] 29 → 30
    [ThreadPoolExecutor-0_6] 30 → 31
    [ThreadPoolExecutor-0_6] 31 → 32
    [ThreadPoolExecutor-0_6] 32 → 33
    [ThreadPoolExecutor-0_6] 33 → 34
    [ThreadPoolExecutor-0_6] 34 → 35
    [ThreadPoolExecutor-0_6] 35 → 36
    [ThreadPoolExecutor-0_6] 36 → 37
    [ThreadPoolExecutor-0_6] 37 → 38
    [ThreadPoolExecutor-0_6] 38 → 39
    [ThreadPoolExecutor-0_6] 39 → 40
    [ThreadPoolExecutor-0_6] 40 → 41
    [ThreadPoolExecutor-0_6] 41 → 42
    [ThreadPoolExecutor-0_6] 42 → 43
    [ThreadPoolExecutor-0_6] 43 → 44
    [ThreadPoolExecutor-0_6] 44 → 45
    [ThreadPoolExecutor-0_6] 45 → 46
    [ThreadPoolExecutor-0_5] 46 → 47
    [ThreadPoolExecutor-0_5] 47 → 48
    [ThreadPoolExecutor-0_5] 48 → 49
    [ThreadPoolExecutor-0_5] 49 → 50
    [ThreadPoolExecutor-0_5] 50 → 51
    [ThreadPoolExecutor-0_5] 51 → 52
    [ThreadPoolExecutor-0_5] 52 → 53
    [ThreadPoolExecutor-0_5] 53 → 54
    [ThreadPoolExecutor-0_5] 54 → 55
    [ThreadPoolExecutor-0_5] 55 → 56
    [ThreadPoolExecutor-0_5] 56 → 57
    [ThreadPoolExecutor-0_5] 57 → 58
    [ThreadPoolExecutor-0_5] 58 → 59
    [ThreadPoolExecutor-0_5] 59 → 60
    [ThreadPoolExecutor-0_5] 60 → 61
    [ThreadPoolExecutor-0_5] 61 → 62
    [ThreadPoolExecutor-0_2] 62 → 63
    [ThreadPoolExecutor-0_8] 63 → 64
    [ThreadPoolExecutor-0_1] 64 → 65
    [ThreadPoolExecutor-0_4] 65 → 66
    [ThreadPoolExecutor-0_4] 66 → 67
    [ThreadPoolExecutor-0_0] 67 → 68
    [ThreadPoolExecutor-0_0] 68 → 69
    [ThreadPoolExecutor-0_9] 69 → 70
    [ThreadPoolExecutor-0_7] 70 → 71
    [ThreadPoolExecutor-0_7] 71 → 72
    [ThreadPoolExecutor-0_7] 72 → 73
    [ThreadPoolExecutor-0_7] 73 → 74
    [ThreadPoolExecutor-0_7] 74 → 75
    [ThreadPoolExecutor-0_7] 75 → 76
    [ThreadPoolExecutor-0_7] 76 → 77
    [ThreadPoolExecutor-0_7] 77 → 78
    [ThreadPoolExecutor-0_7] 78 → 79
    [ThreadPoolExecutor-0_7] 79 → 80
    [ThreadPoolExecutor-0_7] 80 → 81
    [ThreadPoolExecutor-0_7] 81 → 82
    [ThreadPoolExecutor-0_7] 82 → 83
    [ThreadPoolExecutor-0_7] 83 → 84
    [ThreadPoolExecutor-0_7] 84 → 85
    [ThreadPoolExecutor-0_7] 85 → 86
    [ThreadPoolExecutor-0_7] 86 → 87
    [ThreadPoolExecutor-0_7] 87 → 88
    [ThreadPoolExecutor-0_7] 88 → 89
    [ThreadPoolExecutor-0_7] 89 → 90
    [ThreadPoolExecutor-0_7] 90 → 91
    [ThreadPoolExecutor-0_9] 91 → 92
    [ThreadPoolExecutor-0_2] 92 → 93
    [ThreadPoolExecutor-0_5] 93 → 94
    [ThreadPoolExecutor-0_4] 94 → 95
    [ThreadPoolExecutor-0_8] 95 → 96
    [ThreadPoolExecutor-0_1] 96 → 97
    [ThreadPoolExecutor-0_3] 97 → 98
    [ThreadPoolExecutor-0_0] 98 → 99
    [ThreadPoolExecutor-0_6] 99 → 100
    
     最终计数：100
"""
