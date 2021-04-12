# Adapted from https://www.sqlitetutorial.net/sqlite-python/creating-database/
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def search_file(db_file, mfp):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        sql = '''SELECT c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, 1 
                 FROM pgm WHERE upper(pathfile) = upper(?)'''
        cur = conn.cursor()
        cur.execute(sql, (mfp,))
        print("DB Query - search_file")
        myrow = cur.fetchone()
        if myrow is None:
            myrow = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return myrow

def search_files_db(db_file, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        sql = '''SELECT pathfile 
                 FROM pgm WHERE '''
        sqlparam = []
        if c2 > 0:
            sql = sql + 'c2 & ? >= ? and '
            sqlparam.append(c2)
            sqlparam.append(c2)
        if c3 > 0:
            sql = sql + 'c3 & ? >= ? and '
            sqlparam.append(c3)
            sqlparam.append(c3)
        if c4 > 0:
            sql = sql + 'c4 & ? >= ? and '
            sqlparam.append(c4)
            sqlparam.append(c4)
        if c5 > 0:
            sql = sql + 'c5 & ? >= ? and '
            sqlparam.append(c5)
            sqlparam.append(c5)
        if c6 > 0:
            sql = sql + 'c6 & ? >= ? and '
            sqlparam.append(c6)
            sqlparam.append(c6)
        if c7 > 0:
            sql = sql + 'c7 & ? >= ? and '
            sqlparam.append(c7)
            sqlparam.append(c7)
        if c8 > 0:
            sql = sql + 'c8 & ? >= ? and '
            sqlparam.append(c8)
            sqlparam.append(c8)
        if c9 > 0:
            sql = sql + 'c9 & ? >= ? and '
            sqlparam.append(c9)
            sqlparam.append(c9)
        if c10 > 0:
            sql = sql + 'c10 & ? >= ? and '
            sqlparam.append(c10)
            sqlparam.append(c10)
        if c11 > 0:
            sql = sql + 'c11 & ? >= ? and '
            sqlparam.append(c11)
            sqlparam.append(c11)
        if c12 > 0:
            sql = sql + 'c12 & ? >= ? and '
            sqlparam.append(c12)
            sqlparam.append(c12)
        sql = sql + ' 1 = 1'
        cur = conn.cursor()
        cur.execute(sql, sqlparam)
        #cur.execute(sql, (c2,))
        print("DB Query - search_files_db")
        myrows = cur.fetchall()
        for row in myrows:
            print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return myrows

def insert_db(db_file, mfp, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        sql = '''INSERT INTO pgm(pathfile, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        mydata = (mfp, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)
        cur.execute(sql, mydata)
        conn.commit()
        print("DB Insert")
        print(cur.lastrowid)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def update_db(db_file, mfp, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        sql = '''UPDATE pgm SET c1 = ?, c2 = ?, c3 = ?, c4 = ?, c5 = ?, c6 = ?, c7 = ?, c8 = ?, c9 = ?, c10 = ?,
                 c11 = ?, c12 = ?, c13 = ?, c14 = ?, c15 = ?, c16 = ?, c17 = ?, c18 = ?, c19 = ?, c20 = ?
                 WHERE pathfile = ?'''
        cur = conn.cursor()
        mydata = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, mfp)
        cur.execute(sql, mydata)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r"E:\\ablage\\ksfe_2021\\prgsieve\sieve.db")