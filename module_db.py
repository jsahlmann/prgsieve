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
                 FROM pgm WHERE pathfile = ?'''
        cur = conn.cursor()
        cur.execute(sql, (mfp,))
        print("DB Query")
        myrow = cur.fetchone()
        if myrow is None:
            myrow = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return myrow

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