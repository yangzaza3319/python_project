# 测试`__name__`

print("准备导入 module_demo 模块...")

import module_demo as md

print(f"导入成功！当前 md.__name__ = {md.__name__}")

# 调用模块中的函数
result = md.add(10, 20)
print(f"md.add(10, 20) = {result}")

print("测试完成。")