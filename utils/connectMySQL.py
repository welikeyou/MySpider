#连接数据库
import MySQLdb
def connect_mySQL():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="goodsdescirbetion")
    cur = conn.cursor()
    cur.execute("INSERT INTO goods(types,characters) VALUES ('shoes','this is a great goods')")
    cur.close()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_mySQL()
