import sqlite3

# 连接到数据库
conn = sqlite3.connect('tro.db')
c = conn.cursor()

# 执行查询

c.execute("SELECT * FROM esp32_aht15 WHERE topic = '數據回傳序列埠'")
# 获取查询结果
rows = c.fetchall()
for row in rows:
    print(row)

# 关闭连接
conn.close()
