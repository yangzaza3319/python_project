db_type = input("请选择你的数据库类型(mysql/oracle)>>:")

if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db

db.sqlparse()

"""
输出
请选择你的数据库类型(mysql/oracle)>>:mysql
from mysql sqlparse,sqlparse是用于语法分析和美化sql代码的模块

请选择你的数据库类型(mysql/oracle)>>:oracle
from oracle sqlparse,sqlparse是用于语法分析和美化sql代码的模块
"""