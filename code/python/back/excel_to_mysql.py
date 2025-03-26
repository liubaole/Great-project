# 导入 pandas 库，用于数据处理，比如读取 Excel 文件和操作数据框
import pandas as pd
# 导入 mysql.connector 库，用于连接和操作 MySQL 数据库
import mysql.connector

# 定义 Excel 文件的路径，这里使用原始字符串，避免转义字符的影响
file_path = r'F:\TestFile\随访任务数据已随访导出_20250324104653.xlsx'

try:
    # 使用 pandas 的 read_excel 函数读取指定路径的 Excel 文件，并将数据存储在 DataFrame 对象 df 中
    df = pd.read_excel(file_path)
except FileNotFoundError:
    # 如果文件不存在，捕获 FileNotFoundError 异常，并打印错误信息
    print(f"错误：未找到文件 {file_path}")
except Exception as e:
    # 如果在读取文件过程中出现其他异常，捕获该异常并打印具体的错误信息
    print(f"读取文件时发生错误: {e}")
    # 将 df 赋值为 None，表示文件读取失败
    df = None

# 检查 df 是否为 None，如果不为 None 则表示文件读取成功
if df is not None:
    try:
        # 尝试连接到 MySQL 数据库
        connection = mysql.connector.connect(
            # 数据库所在的主机地址
            host='localhost',
            # 数据库使用的端口号
            port=3306,
            # 连接数据库的用户名
            user='root',
            # 连接数据库的密码
            password='123456',
            # 要使用的数据库名称
            database='bigdata'
        )
        # 创建一个游标对象，用于执行 SQL 语句
        cursor = connection.cursor()

        # 用反引号括起 DataFrame 的列名，以处理列名包含特殊字符的情况
        columns = '`, `'.join(df.columns)
        columns = f'`{columns}`'
        # 生成与列数相同数量的占位符，用于 SQL 插入语句
        placeholders = ', '.join(['%s'] * len(df.columns))
        # 构建插入数据的 SQL 语句，指定要插入数据的表名和列名，以及使用占位符表示要插入的值
        insert_query = f"INSERT INTO patientdata ({columns}) VALUES ({placeholders})"

        # 遍历 DataFrame 的每一行数据
        for row in df.values.tolist():
            # 执行插入数据的 SQL 语句，将每一行数据插入到数据库中
            cursor.execute(insert_query, row)

        # 提交事务，将所有插入操作保存到数据库中
        connection.commit()
        # 打印数据插入成功的信息
        print("数据已成功插入数据库。")

    except mysql.connector.Error as err:
        # 如果在数据库操作过程中出现错误，捕获该异常并打印具体的错误信息
        print(f"数据库操作出错: {err}")
    finally:
        # 无论数据库操作是否成功，都会执行该部分代码
        if connection.is_connected():
            # 如果数据库连接仍然处于打开状态，关闭游标
            cursor.close()
            # 关闭数据库连接
            connection.close()
            # 打印数据库连接已关闭的信息
            print("数据库连接已关闭。")
