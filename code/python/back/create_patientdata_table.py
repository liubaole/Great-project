import mysql.connector

# 数据库连接配置
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'port': 3306,
    'database': 'bigdata'
}

try:
    # 建立数据库连接
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # 创建 patientData 表的 SQL 语句
    create_table_query = """
    CREATE TABLE IF NOT EXISTS patientData (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        tepy VARCHAR(255),
        class VARCHAR(255),
        state VARCHAR(255),
        institution VARCHAR(255),
        follow_up_doctor VARCHAR(255),
        plan_follow_up_time DATE,
        follow_up_way VARCHAR(255),
        follow_up_time DATETIME
    )
    """

    # 执行 SQL 语句
    cursor.execute(create_table_query)
    connection.commit()
    print("表 patientData 创建成功！")

except mysql.connector.Error as err:
    print(f"发生错误: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
