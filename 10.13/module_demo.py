# 全局变量 __name__

def add(a, b):
    return a + b

# 只有直接运行时才执行测试
if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))  # 输出: 5