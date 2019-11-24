"""利用Pycharm向数据库里查询数据"""
import pymysql

conn  = pymysql.connect(
    host = 'localhost',
    port =3306,
    user='root',
    password='Yuhang929',
    database='school',
    charset='utf8'
)

try:
    with conn.cursor() as cursor:
        cursor.execute(
            'select stuid, stuname, stuaddr, collname from tb_student t1 '
            'inner join tb_college t2 on t1.collid = t2.collid '
            'order by stuid limit 7 offset 2'
        )
        for row in cursor.fetchall():
            print(row)
except pymysql.MySQLError as err:
    print(err)
finally:
    conn.close()