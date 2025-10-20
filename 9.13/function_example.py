# 案例1 简单计算器的实现 
def calculate(operation, num1 , num2):
    """简单计算器实现"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "错误：除数不能为零！"
        return num1 / num2
    else:
        return "错误：未知操作！"

# 用户输入
user_operation = input("请输入操作（add, subtract, multiply, divide）: ")
user_num1 = float(input("请输入第一个数字: "))
user_num2 = float(input("请输入第二个数字: "))

# 调用函数
result = calculate(user_operation, user_num1, user_num2)
print(f"结果: {result}")


# 案例2 书籍入库管理

def add_book(book_title,book_id, *authors, **details):
    """
    添加书籍信息并打印
    """
    print("********************")
    print(f"书籍名称：《{book_title}》")
    print(f"书籍编号：{book_id}")
    print(f"作者：{','.join(authors)}")
    for key, value in details.items():
        print(f"{key}:{value}")
    print("-----")

# 添加书籍
add_book("四世同堂",101,"老舍",备注="1990s",others="小说")
add_book("傅雷家书",102,"傅雷",备注="傅氏家族的育儿观")
add_book("四库全书",103,"明朝人士",备注="一本古代的百科全书")
