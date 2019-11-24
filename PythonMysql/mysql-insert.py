"""利用Pycharm向数据库里插入数据"""
import pymysql


name = input('学院名称:')
intro = input('学院介绍:')

conn = pymysql.connect(host='localhost',port =3306,user='root',password='Yuhang929',database='school',charset='utf8')

try:
    with conn.cursor() as cursor:
        result = cursor.execute(
            'insert into tb_college values (default,%s ,%s)',
            (name,intro)
        )
        if result ==1:
            print('新增学院成功!!!')
    conn.commit()
except pymysql.MySQLError as err:
    print(err)
    conn.rollback()
finally:
    conn.close()