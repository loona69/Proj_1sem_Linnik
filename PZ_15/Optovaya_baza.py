import sqlite3 as sq
from data_opt import info_gds, info_shp, info_apl, info_stk, info_cmd

with sq.connect('opt_baza.db') as con:
    cur.execute("""CREATE TABLE IF NOT EXISTS gds (
        id_g INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50), 
        descript VARCHAR(100),
        unit VARCHAR(50)
        ) """)

with sq.connect('opt_baza.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO gds VALUES (?, ?, ?, ?)", info_gds)
    con.commit

with sq.connect('opt_baza.db') as con:
    cur.execute("""CREATE TABLE IF NOT EXISTS shp (
        id_s INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(25), 
        ads VARCHAR(50),
        numb VARCHAR(20)
        ) """)

with sq.connect('opt_baza.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO shp VALUES (?, ?, ?, ?)", info_shp)
    con.commit

with sq.connect('opt_baza.db') as con:
    cur.execute("""CREATE TABLE IF NOT EXISTS apl (
        id_a INTEGER PRIMARY KEY AUTOINCREMENT,
        id_s INTEGER, 
        d_a DATE,
        FOREIGN KEY (id_s) REFERENCES shp(id_s) ON DELETE CASCADE ON UPDATE CASCADE
        ) """)

with sq.connect('opt_baza.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO shp VALUES (?, ?, ?)", info_apl)
    con.commit

with sq.connect('opt_baza.db') as con:
    cur.execute("""CREATE TABLE IF NOT EXISTS stk (
        id_stk INTEGER PRIMARY KEY AUTOINCREMENT,
        id_g INTEGER, 
        quant INTEGER,
        FOREIGN KEY (id_g) REFERENCES gds(id_g) ON DELETE CASCADE ON UPDATE CASCADE
        ) """)

with sq.connect('opt_baza.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO shp VALUES (?, ?, ?)", info_stk)
    con.commit

with sq.connect('opt_baza.db') as con:
    cur.execute("""CREATE TABLE IF NOT EXISTS cmd (
        id_c INTEGER PRIMARY KEY AUTOINCREMENT,
        id_a INTEGER, 
        id_g INTEGER,
        quant INTEGER,
        FOREIGN KEY (id_a) REFERENCES apl(id_a) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (id_g) REFERENCES gds(id_g) ON DELETE CASCADE ON UPDATE CASCADE
        ) """)

with sq.connect('opt_baza.db') as con:
    cur = con.cursor()
    con.executemany("INSERT INTO cmd VALUES (?, ?, ?)", info_cmd)
    con.commit

# selecti

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, descript FROM gds")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, ads FROM shp")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT shp.name, apl.d_a FROM shp INNER JOIN apl ON shp.id_s = apl.id_s")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT gds.name, stk.quant FROM gds INNER JOIN stock ON gds.id_g = stk.id_g")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT gds.name, stk.quant FROM gds INNER JOIN stk ON gds.id_g = stk.id_g ORDER BY stk.quant DESC")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT apl.id_a, shp.name, gds.name FROM apl JOIN stores ON apl.id_s = apl.id_s JOIN cmd ON apl.id_a = cmd.id_a JOIN gds ON cmd.id_g = gds.id_g")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM apl WHERE d_a BETWEEN '2023-01-01' AND '2023-04-16'")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT shp.name FROM shp JOIN stk ON shp.id_stk = stk.id_stk GROUP BY shp.id_s HAVING SUM(stk.quant) < 10")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT name FROM stk JOIN gds ON stk.id_g = gds.id_g WHERE quant < 10")
#     res = cur.fetchall()
# print(res)


# апдейты


# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stk SET quant = 30 WHERE id_g = 2")

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE cmd SET id_g = 3 WHERE id_g = 2")

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE cmd SET quant = 10 WHERE id_g = 1")

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE shp SET ads = 'ул. ГВидона ХМельницкого, д. 15' WHERE id_s = 2")

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE apl SET d_a = '2023-03-28' WHERE id_s = 1")

# делиты

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM apl WHERE id_s IN (SELECT id_s FROM shp WHERE ads LIKE 'ул. Ленина%')")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM cmd WHERE cmd.id_g IN (SELECT cmd.id_g FROM cmd INNER JOIN stk ON cmd.id_g = cmd.id_g WHERE stk.quant = 0)")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM shp WHERE shp.id_s IN (SELECT shp.id_s FROM shp INNER JOIN apl ON shp.id_s = apl.id_s WHERE apl.a_d BETWEEN '2023-02-01' AND '2023-02-30')")
#     res = cur.fetchall()
# print(res)

# with sq.connect("opt_baza.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM shp WHERE shp.st_id IN (SELECT shp.id_s FROM shp INNER JOIN apl ON shp.id_s = apl.id_s WHERE apl.d_a BETWEEN '2023-02-01' AND '2023-02-30')")
#     res = cur.fetchall()
# print(res)

with sq.connect("opt_baza.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM gds WHERE id_g NOT IN (SELECT id_g FROM cmd LEFT JOIN gds ON cmd.id_g = gds.id_g)")
    res = cur.fetchall()
print(res)