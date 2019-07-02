import pymysql


class MySQL:
    def __init__(self):
        pass

    def conn(self, conn, user, password, db):
        db = pymysql.connect(conn, user, password, db, charset='utf8')
        return db

    def exe(self, sql):
        db = self.conn("60.205.107.112", "root", "Wanlingyun1234.", "CiMing")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        return cursor.fetchall()
